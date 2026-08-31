#!/usr/bin/env python3
"""Gemeinsame Helfer fuer Export, Konvertierung und Asset-Download."""
import json, os, re, unicodedata

HOST = "https://diysynth.wiki.dsl-man.de"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "raw")
CONTENT = os.path.join(ROOT, "content")

UMLAUT = {"ä": "ae", "ö": "oe", "ü": "ue", "Ä": "ae", "Ö": "oe", "Ü": "ue", "ß": "ss"}


def slugify(text, maxlen=70):
    """Titel -> URL-tauglicher Ordnername."""
    text = (text or "").strip()
    for k, v in UMLAUT.items():
        text = text.replace(k, v)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    text = re.sub(r"-{2,}", "-", text)
    if len(text) > maxlen:
        text = text[:maxlen].rsplit("-", 1)[0] or text[:maxlen]
    return text or "seite"


def asset_name(filename):
    """Anhangsname -> dateisystem- und URL-freundlicher Name, Endung bleibt."""
    base, ext = os.path.splitext(filename or "datei")
    for k, v in UMLAUT.items():
        base = base.replace(k, v)
    base = unicodedata.normalize("NFKD", base)
    base = "".join(c for c in base if not unicodedata.combining(c))
    base = re.sub(r"[^A-Za-z0-9._-]+", "-", base).strip("-._") or "datei"
    if len(base) > 90:
        base = base[:90]
    ext = re.sub(r"[^A-Za-z0-9.]+", "", ext).lower()
    return base + ext


def load(name):
    with open(os.path.join(RAW, name)) as f:
        return json.load(f)


def build_model():
    """Baut das Seitenmodell: Hierarchie, Zielpfade, Anhangszuordnung."""
    spaces = {s["id"]: s for s in load("spaces.json")}
    pages = load("pages.json")
    blogs = load("blogposts.json")
    atts = load("attachments.json")

    space_slug = {}
    used = set()
    for s in spaces.values():
        sl = slugify(s["name"]) or s["key"].lower()
        while sl in used:
            sl = sl + "-" + s["key"].lower()
        used.add(sl)
        space_slug[s["id"]] = sl
        s["slug"] = sl

    by_id = {}
    for p in pages:
        p["kind"] = "page"
        by_id[p["id"]] = p
    for b in blogs:
        b["kind"] = "blogpost"
        by_id[b["id"]] = b

    # Homepage je Space = Space-Wurzel
    homepages = {str(s.get("homepageId")): s["id"] for s in spaces.values() if s.get("homepageId")}

    def chain(p):
        out, seen = [], set()
        cur = p
        while cur is not None and cur["id"] not in seen:
            seen.add(cur["id"])
            out.append(cur)
            pid = cur.get("parentId")
            cur = by_id.get(str(pid)) if pid else None
        return list(reversed(out))

    taken = {}
    for p in sorted(by_id.values(), key=lambda x: (x.get("spaceId", ""), len(chain(x)), x.get("title") or "")):
        sl = space_slug.get(p.get("spaceId"), "misc")
        if p["kind"] == "blogpost":
            day = (p.get("createdAt") or "")[:10]
            parts = [sl, "blog", "%s-%s" % (day, slugify(p.get("title")))]
        elif str(p["id"]) in homepages and not p.get("parentId"):
            parts = [sl]
        else:
            ch = chain(p)
            if ch and str(ch[0]["id"]) in homepages:
                ch = ch[1:]          # Space-Startseite ist bereits der Space-Ordner
            parts = [sl] + [slugify(a.get("title")) for a in ch]
        base = "/".join(parts)
        cand, n = base, 1
        while cand in taken and taken[cand] != p["id"]:
            n += 1
            cand = "%s-%d" % (base, n)
        taken[cand] = p["id"]
        p["path"] = cand
        p["space_slug"] = sl

    # Anhaenge ihren Seiten zuordnen
    for p in by_id.values():
        p["attachments"] = []
    orphans = []
    seen_files = {}
    for a in sorted(atts, key=lambda x: str(x.get("id"))):
        cid = str((a.get("container") or {}).get("id", ""))
        fn = asset_name(a.get("title"))
        key = (cid, fn.lower())
        if key in seen_files:                 # gleicher Dateiname auf derselben Seite
            base, ext = os.path.splitext(fn)
            seen_files[key] += 1
            fn = "%s-%d%s" % (base, seen_files[key], ext)
        else:
            seen_files[key] = 1
        a["file"] = fn
        if cid in by_id:
            by_id[cid]["attachments"].append(a)
        else:
            orphans.append(a)

    # Titelindex fuer interne Links: (spaceKey, titel) -> Seite
    title_idx = {}
    for p in by_id.values():
        title_idx[(p.get("spaceKey"), (p.get("title") or "").strip())] = p

    return {"spaces": spaces, "pages": by_id, "title_idx": title_idx,
            "orphan_attachments": orphans, "space_slug": space_slug}

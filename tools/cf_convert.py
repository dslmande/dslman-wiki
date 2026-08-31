#!/usr/bin/env python3
"""Erzeugt aus dem Roh-Export das Markdown-Repo unter content/."""
import os, re, shutil, sys, collections
from urllib.parse import unquote
import cflib
from storage2md import Converter, IMG_EXT

HOST = cflib.HOST


def yaml_str(s):
    return '"%s"' % (s or "").replace("\\", "\\\\").replace('"', '\\"')


class Site:
    def __init__(self):
        self.m = cflib.build_model()
        self.pages = self.m["pages"]
        self.title_idx = self.m["title_idx"]
        self.by_num = {str(p["id"]): p for p in self.pages.values()}
        self.unknown = collections.Counter()
        self.missing_assets = collections.Counter()
        self.dead_links = collections.Counter()
        self.url_map = []
        self.space_home = {}
        for sp in self.m["spaces"].values():
            hp = self.by_num.get(str(sp.get("homepageId")))
            if hp is not None:
                self.space_home[sp["key"]] = hp

    # ---- Linkaufloesung ----
    def rel(self, src, dst_path, anchor=""):
        """Relativer Markdown-Link von Seite src zu Zielpfad."""
        base = os.path.dirname(src["path"] + "/x")
        r = os.path.relpath(dst_path + "/index.md", base)
        return r + anchor

    def page_link(self, src, title, space_key):
        key = space_key or src.get("spaceKey")
        tgt = self.title_idx.get((key, (title or "").strip()))
        if tgt is None:                       # spaceuebergreifend suchen
            cands = [p for (k, t), p in self.title_idx.items() if t == (title or "").strip()]
            tgt = cands[0] if len(cands) == 1 else None
        if tgt is None:
            self.dead_links[title] += 1
            return "#"
        return self.rel(src, tgt["path"])

    def url(self, src, href):
        """Absolute Confluence-URLs auf lokale Seiten umbiegen."""
        if not href:
            return href
        if HOST in href or "dsl-man.atlassian.net" in href or href.startswith("/wiki/"):
            # Direktlink auf einen Anhang: /download/attachments/<pageId>/<datei>
            m = re.search(r"/download/(?:attachments|thumbnails)/(\d+)/([^?#]+)", href)
            if m:
                tgt = self.by_num.get(m.group(1))
                fn = cflib.asset_name(unquote(m.group(2)))
                if tgt is not None:
                    return os.path.relpath(os.path.join(tgt["path"], "assets", fn),
                                           os.path.dirname(src["path"] + "/x"))
            m = re.search(r"/pages/(\d+)|[?&]pageId=(\d+)", href)
            pid = (m.group(1) or m.group(2)) if m else None
            if pid and pid in self.by_num:
                anchor = ("#" + href.split("#", 1)[1]) if "#" in href else ""
                return self.rel(src, self.by_num[pid]["path"], anchor)
            m = re.search(r"/(?:display|spaces)/([A-Za-z0-9~._-]+)/?([^?#]*)", href)
            if m:
                title = unquote(m.group(2).replace("+", " ")).split("/")[-1].strip()
                if title:
                    return self.page_link(src, title, m.group(1))
                home = self.space_home.get(m.group(1))      # Link auf die Space-Startseite
                if home is not None:
                    return self.rel(src, home["path"])
            self.dead_links[href[:90]] += 1
        return href

    # ---- Anhaenge ----
    def asset(self, src, filename):
        fn = cflib.asset_name(filename)
        if not any(a["file"] == fn for a in src["attachments"]):
            for p in self.pages.values():     # Anhang einer anderen Seite?
                if any(a["file"] == fn for a in p["attachments"]):
                    return os.path.relpath(os.path.join(p["path"], "assets", fn),
                                           os.path.dirname(src["path"] + "/x"))
            self.missing_assets[filename] += 1
        return "assets/" + fn

    def has_asset(self, src, filename):
        fn = cflib.asset_name(filename)
        return any(a["file"] == fn for a in src["attachments"])

    def gallery(self, src):
        imgs = [a for a in src["attachments"] if a["file"].lower().endswith(IMG_EXT)]
        return "\n\n".join("![%s](assets/%s)" % (a.get("title", ""), a["file"]) for a in imgs)

    def attachment_list(self, src):
        return "\n".join("- [%s](assets/%s)" % (a.get("title", ""), a["file"])
                         for a in src["attachments"])

    # ---- Seite schreiben ----
    def render(self, p):
        ctx = {
            "asset": lambda f: self.asset(p, f),
            "has_asset": lambda f: self.has_asset(p, f),
            "page": lambda t, k: self.page_link(p, t, k),
            "url": lambda u: self.url(p, u),
            "gallery": lambda: self.gallery(p),
            "attachment_list": lambda: self.attachment_list(p),
        }
        conv = Converter(ctx)
        body = ((p.get("body") or {}).get("storage") or {}).get("value", "")
        md, unk = conv.convert(body)
        self.unknown.update(unk)

        space = self.m["spaces"].get(p.get("spaceId"), {})
        src_url = "%s/wiki/spaces/%s/pages/%s" % (HOST, p.get("spaceKey", ""), p["id"])
        fm = [
            "---",
            "title: " + yaml_str(p.get("title")),
            "space: " + yaml_str(space.get("name") or p.get("spaceKey")),
            "space_key: " + yaml_str(p.get("spaceKey")),
            "type: " + p["kind"],
            "created: " + yaml_str((p.get("createdAt") or "")[:19]),
            "updated: " + yaml_str(((p.get("version") or {}).get("createdAt") or "")[:19]),
            "confluence_id: " + yaml_str(str(p["id"])),
            "confluence_url: " + yaml_str(src_url),
        ]
        atts = [a for a in p["attachments"]]
        if atts:
            fm.append("attachments: %d" % len(atts))
        fm.append("---\n")

        title = "# " + (p.get("title") or "").strip() + "\n\n"
        out = "\n".join(fm) + "\n" + title + md
        dest = os.path.join(cflib.CONTENT, p["path"], "index.md")
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w") as f:
            f.write(out)
        self.url_map.append((src_url, "/" + p["path"] + "/"))
        return len(out)


def main():
    fresh = "--keep" not in sys.argv
    if fresh and os.path.isdir(cflib.CONTENT):
        # Assets stehen im selben Baum: nur .md-Dateien neu erzeugen
        for root, _, files in os.walk(cflib.CONTENT):
            for f in files:
                if f.endswith(".md"):
                    os.remove(os.path.join(root, f))
    s = Site()
    total = 0
    for p in sorted(s.pages.values(), key=lambda x: x["path"]):
        total += s.render(p)
    print("Seiten geschrieben: %d (%.1f MB Markdown)" % (len(s.pages), total / 1e6))

    with open(os.path.join(cflib.RAW, "url-map.csv"), "w") as f:
        f.write("confluence_url,neuer_pfad\n")
        for a, b in sorted(s.url_map):
            f.write("%s,%s\n" % (a, b))

    rep = [
        "Unbekannte Makros (Inhalt bleibt erhalten, Darstellung pruefen):",
    ] + ["  %-28s %d" % (k, v) for k, v in s.unknown.most_common()] + [
        "", "Nicht aufgeloeste Links: %d" % sum(s.dead_links.values()),
    ] + ["  %-60s %d" % (k, v) for k, v in s.dead_links.most_common(25)] + [
        "", "Fehlende Anhaenge: %d" % sum(s.missing_assets.values()),
    ] + ["  %-60s %d" % (k, v) for k, v in s.missing_assets.most_common(25)]
    open(os.path.join(cflib.RAW, "convert-report.txt"), "w").write("\n".join(rep) + "\n")
    print("\n".join(rep[:14]))


if __name__ == "__main__":
    main()

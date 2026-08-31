#!/usr/bin/env python3
"""Holt den kompletten Confluence-Cloud-Inhalt als Roh-JSON nach raw/.

Anonymer Lesezugriff genuegt; alle Requests laufen ueber curl, weil das
System-Python kein CA-Bundle hat.
"""
import json, os, subprocess, sys, time, urllib.parse

HOST = "https://diysynth.wiki.dsl-man.de"
BASE = HOST + "/wiki"
RAW = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "raw")


def curl(url, tries=4):
    if url.startswith("/rest/") or url.startswith("/api/"):
        url = BASE + url          # Cursor-Links kommen relativ zu /wiki
    elif url.startswith("/"):
        url = HOST + url
    for n in range(tries):
        p = subprocess.run(["curl", "-sS", "--compressed", "--max-time", "60", url],
                           capture_output=True, text=True)
        if p.returncode == 0:
            try:
                return json.loads(p.stdout)
            except ValueError:
                pass
        time.sleep(2 * (n + 1))
    raise SystemExit("FEHLER bei %s" % url)


def paged_v2(url):
    """v2-API: Cursor-Pagination ueber _links.next."""
    out = []
    while url:
        d = curl(url)
        out += d.get("results", [])
        url = d.get("_links", {}).get("next")
    return out


def paged_cql(cql, expand, limit=100):
    """v1-Suche: Cursor-Pagination (der Parameter `start` wird ignoriert)."""
    url = "%s/rest/api/content/search?limit=%d&expand=%s&cql=%s" % (
        BASE, limit, expand, urllib.parse.quote(cql))
    out, seen = [], set()
    while url:
        d = curl(url)
        res = d.get("results", [])
        new_ids = [r for r in res if r.get("id") not in seen]
        if not new_ids:
            break
        for r in new_ids:
            seen.add(r.get("id"))
        out += new_ids
        nxt = d.get("_links", {}).get("next")
        url = nxt if nxt else None
    return out


def main():
    os.makedirs(RAW, exist_ok=True)
    spaces = paged_v2(BASE + "/api/v2/spaces?limit=100")
    json.dump(spaces, open(os.path.join(RAW, "spaces.json"), "w"), indent=1)
    print("Spaces: %d" % len(spaces))

    all_pages, all_blogs, all_atts = [], [], []
    for s in spaces:
        key, sid = s["key"], s["id"]
        pages = paged_v2("%s/api/v2/spaces/%s/pages?limit=50&body-format=storage" % (BASE, sid))
        blogs = paged_v2("%s/api/v2/spaces/%s/blogposts?limit=50&body-format=storage" % (BASE, sid))
        atts = paged_cql('space="%s" and type=attachment' % key, "container,version,extensions")
        for c in pages + blogs:
            c["spaceKey"] = key
        for a in atts:
            a["spaceKey"] = key
        all_pages += pages
        all_blogs += blogs
        all_atts += atts
        print("  %-14s Seiten %4d  Blog %3d  Anhaenge %5d" % (key, len(pages), len(blogs), len(atts)))
        sys.stdout.flush()

    json.dump(all_pages, open(os.path.join(RAW, "pages.json"), "w"), indent=1)
    json.dump(all_blogs, open(os.path.join(RAW, "blogposts.json"), "w"), indent=1)
    json.dump(all_atts, open(os.path.join(RAW, "attachments.json"), "w"), indent=1)

    total = sum(a.get("extensions", {}).get("fileSize", 0) or 0 for a in all_atts)
    print("\nGESAMT: %d Seiten, %d Blogposts, %d Anhaenge (%.1f GB)" % (
        len(all_pages), len(all_blogs), len(all_atts), total / 1e9))


if __name__ == "__main__":
    main()

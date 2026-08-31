#!/usr/bin/env python3
"""Prueft das erzeugte Repo: verweisen alle Links und Bilder auf echte Dateien?"""
import os, re, sys, collections
from urllib.parse import unquote
import cflib

LINK = re.compile(r"(!?)\[([^\]]*)\]\(([^)]+)\)")


def main():
    bad_md, bad_asset, ok, ext_links, anchors = [], [], 0, 0, 0
    unused = set()
    used = set()
    for root, _, files in os.walk(cflib.CONTENT):
        for f in files:
            if f != "index.md":
                if "/assets" in root.replace(os.sep, "/"):
                    unused.add(os.path.join(root, f))
                continue
            path = os.path.join(root, f)
            text = open(path).read()
            for bang, label, href in LINK.findall(text):
                href = href.strip()
                if href.startswith(("http://", "https://", "mailto:")):
                    ext_links += 1
                    continue
                if href.startswith("#"):
                    anchors += 1
                    continue
                target = os.path.normpath(os.path.join(root, unquote(href.split("#")[0])))
                if os.path.exists(target):
                    ok += 1
                    used.add(target)
                elif bang or "/assets/" in href:
                    bad_asset.append((path, href))
                else:
                    bad_md.append((path, href))

    print("Interne Verweise ok:        %d" % ok)
    print("Externe Links:              %d" % ext_links)
    print("Nur Anker:                  %d" % anchors)
    print("Fehlende Seitenziele:       %d" % len(bad_md))
    print("Fehlende Anhaenge:          %d" % len(bad_asset))
    for p, h in bad_asset[:15]:
        print("   %s -> %s" % (os.path.relpath(p, cflib.CONTENT), h))
    for p, h in bad_md[:15]:
        print("   %s -> %s" % (os.path.relpath(p, cflib.CONTENT), h))
    nn = sorted(unused - used)
    print("Nicht verlinkte Anhaenge:   %d (bleiben erhalten, oft Downloadlisten)" % len(nn))
    return 0


if __name__ == "__main__":
    sys.exit(main())

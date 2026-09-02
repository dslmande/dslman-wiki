#!/usr/bin/env python3
"""Rechnet die Bilder auf Webgroesse (max 2000 px, JPEG q82).

Die Originale werden vorher unveraendert nach ORIG_DIR gesichert. HEIC wird
nach JPEG gewandelt; die Umbenennung landet in raw/asset-rewrites.json, damit
cf_convert.py die Markdown-Verweise mitzieht.
"""
import json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
import cflib

ORIG_DIR = os.path.join(os.path.dirname(cflib.ROOT), "dslman-wiki-originale")
MAXPX = "2000"
QUALITY = "75"
JPEG = (".jpg", ".jpeg")
PNGS = (".png",)
HEIC = (".heic", ".heif")
MIN_BYTES = 250_000          # kleinere Bilder lohnen den Verlust nicht


def backup(path):
    """Sichert das Original einmalig und liefert die Quelle fuer die Umrechnung.

    Bei einem zweiten Lauf wird aus dem Original gerechnet, nicht aus dem
    bereits komprimierten Bild - sonst summiert sich der Qualitaetsverlust.
    """
    rel = os.path.relpath(path, cflib.CONTENT)
    dst = os.path.join(ORIG_DIR, rel)
    if os.path.exists(dst):
        return dst
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    subprocess.run(["cp", "-p", path, dst], check=True)
    return dst


def sips(args):
    return subprocess.run(["sips"] + args, capture_output=True).returncode == 0


def work(path):
    ext = os.path.splitext(path)[1].lower()
    before = os.path.getsize(path)
    try:
        if ext in HEIC:
            src = backup(path)
            out = os.path.splitext(path)[0] + ".jpg"
            if sips(["-s", "format", "jpeg", "-Z", MAXPX, "-s", "formatOptions", QUALITY,
                     src, "--out", out]):
                os.remove(path)
                return (before, os.path.getsize(out), os.path.basename(path),
                        os.path.basename(out))
            return (before, before, None, None)
        if before < MIN_BYTES and not os.path.exists(
                os.path.join(ORIG_DIR, os.path.relpath(path, cflib.CONTENT))):
            return (before, before, None, None)
        src = backup(path)
        before = os.path.getsize(src)
        if ext in JPEG:
            sips(["-Z", MAXPX, "-s", "formatOptions", QUALITY, src, "--out", path])
        elif ext in PNGS:
            sips(["-Z", MAXPX, src, "--out", path])
        return (before, os.path.getsize(path), None, None)
    except Exception as e:
        sys.stderr.write("%s: %s\n" % (path, e))
        return (before, before, None, None)


def main():
    targets = []
    for root, _, files in os.walk(cflib.CONTENT):
        for f in files:
            if os.path.splitext(f)[1].lower() in JPEG + PNGS + HEIC:
                targets.append(os.path.join(root, f))
    print("Bilder: %d  |  Originale werden gesichert nach %s" % (len(targets), ORIG_DIR))

    rewrites, before_sum, after_sum, n = {}, 0, 0, 0
    with ThreadPoolExecutor(max_workers=8) as ex:
        for b, a, old, new in ex.map(work, targets):
            before_sum += b
            after_sum += a
            if old:
                rewrites[old] = new
            n += 1
            if n % 250 == 0:
                print("  %d/%d  (%.2f -> %.2f GB)" % (n, len(targets), before_sum / 1e9, after_sum / 1e9), flush=True)

    json.dump(rewrites, open(os.path.join(cflib.RAW, "asset-rewrites.json"), "w"), indent=1)
    print("\nBilder: %.2f GB -> %.2f GB  (%.0f %% gespart), %d Formatwechsel HEIC->JPEG"
          % (before_sum / 1e9, after_sum / 1e9,
             100 * (1 - after_sum / max(before_sum, 1)), len(rewrites)))


if __name__ == "__main__":
    main()

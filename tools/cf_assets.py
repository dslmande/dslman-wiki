#!/usr/bin/env python3
"""Laedt alle Anhaenge in den assets/-Ordner der jeweiligen Seite."""
import os, subprocess, sys, cflib

HOST = cflib.HOST
PAR = 8   # parallele Downloads


def main():
    m = cflib.build_model()
    jobs = []
    for p in m["pages"].values():
        d = os.path.join(cflib.CONTENT, p["path"], "assets")
        for a in p["attachments"]:
            dl = (a.get("_links") or {}).get("download")
            if not dl:
                continue
            jobs.append((HOST + "/wiki" + dl if dl.startswith("/") else dl,
                         os.path.join(d, a["file"])))
    for a in m["orphan_attachments"]:
        dl = (a.get("_links") or {}).get("download")
        if dl:
            jobs.append((HOST + "/wiki" + dl,
                         os.path.join(cflib.CONTENT, "_verwaiste-anhaenge", a["file"])))

    todo = [(u, f) for u, f in jobs if not os.path.exists(f)]
    print("Anhaenge gesamt %d, zu laden %d" % (len(jobs), len(todo)))
    for f in set(os.path.dirname(f) for _, f in todo):
        os.makedirs(f, exist_ok=True)

    done = err = 0
    running = []
    for u, f in todo:
        running.append((subprocess.Popen(
            ["curl", "-sS", "-L", "--fail", "--max-time", "300"] + cflib.auth_args()
            + ["-o", f + ".part", u],
            stdout=subprocess.DEVNULL, stderr=subprocess.PIPE), f))
        while len(running) >= PAR:
            done, err = reap(running, done, err)
    while running:
        done, err = reap(running, done, err)
    print("\nFertig: %d geladen, %d Fehler" % (done, err))


def reap(running, done, err):
    for i, (proc, f) in enumerate(list(running)):
        if proc.poll() is not None:
            running.pop(i)
            if proc.returncode == 0 and os.path.exists(f + ".part"):
                os.replace(f + ".part", f)
                done += 1
            else:
                err += 1
                if os.path.exists(f + ".part"):
                    os.remove(f + ".part")
                sys.stderr.write("FEHLER %s\n" % os.path.basename(f))
            if (done + err) % 100 == 0:
                print("  %d/%d" % (done + err, done + err + len(running)), flush=True)
            return done, err
    import time; time.sleep(0.05)
    return done, err


if __name__ == "__main__":
    main()

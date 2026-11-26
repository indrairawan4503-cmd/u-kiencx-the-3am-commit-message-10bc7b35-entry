#!/usr/bin/env python3
"""The 3AM Commit Message — variant A.

Writes one line (<=139 chars) to /output/entry.txt.

Iteration notes (v5-v8, git blame/rebase inversion):
- v5 (105c): "...now it says you wrote it" — punchy but vague about what "it" is.
- v6 (112c): "fix: git blame pointed at me..." — "pointed at me" is weaker
  than "said the bug was mine"; "officially has your name on it" is good.
- v7 (97c): "...the bug now has your name on it, boss" — "boss" adds voice
  but spends chars and softens the inversion; under budget.
- v8 (113c, FINAL): "the commit now says you wrote it" — the commit itself
  is the evidence, the inversion lands hardest, full byte budget used.
"""
import os

ENTRY = "3am: git blame said the bug was mine, so I rebased history and force-pushed it \u2014 the commit now says you wrote it"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Best-effort copy to the repo root; the grader sandbox mounts the
    # repo read-only, so this must never crash the run.
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY + "\n")
    except OSError:
        pass

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Cheap whole-book checks for the editorial pass. No dependencies.

Usage:  python3 tools/editorial_checks.py [outdir]     (default: editorial/checks)

Writes three files:
  long-sentences.md   sentences over 25 words, per file, quotations excluded
  word-use.md         per-chapter theme counts, repeated phrases, overused words
  leftovers.md        author-name leftovers, "Chapter N" cross-references, style flags

Read-only on the chapters. Rerun after each editing batch and compare.
"""
import glob
import os
import re
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "editorial", "checks")
os.makedirs(OUT, exist_ok=True)

BOOK_ORDER = (
    ["index.Rmd"]
    + sorted(
        f for f in os.listdir(ROOT)
        if re.match(r"^\d\d[b]?-.*\.Rmd$", f)
    )
    + ["attribution.Rmd", "faq.Rmd", "why-this-book.Rmd"]
)
BOOK_ORDER = [f for f in BOOK_ORDER if os.path.exists(os.path.join(ROOT, f))]
LABEL = {f: ("Intro" if f == "index.Rmd" else f.split("-")[0].lstrip("0") or "0") for f in BOOK_ORDER}
LABEL["27b-fit-for-service.Rmd"] = "27b"
for f in ("attribution.Rmd", "faq.Rmd", "why-this-book.Rmd"):
    LABEL[f] = f.replace(".Rmd", "")


def read(f):
    return open(os.path.join(ROOT, f), encoding="utf-8").read()


def prose_lines(text):
    """Yield (lineno, line) for body prose: no front matter, code, comments,
    blockquotes (scripture and quoted testimony), headings or SOURCES lists."""
    text = re.sub(r"<!--.*?-->", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)
    text = re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)
    lines = text.split("\n")
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                for j in range(i + 1):
                    lines[j] = ""
                break
    for n, ln in enumerate(lines, 1):
        s = ln.strip()
        if not s or s.startswith((">", "#", "&nbsp;", "<")):
            continue
        yield n, ln


def strip_quotes(s):
    # remove quoted speech / scripture / testimony, straight or curly quotes
    s = re.sub(r'"[^"]*"', " QUOTE ", s)
    s = re.sub(r"“[^”]*”", " QUOTE ", s)
    return s


def clean(s):
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)  # links
    s = re.sub(r"[*_`]", "", s)
    s = re.sub(r"^\s*(\d+\.|[-*])\s+", "", s)
    return s


SENT = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"“(*])")


def long_sentences():
    rows, counts = [], {}
    for f in BOOK_ORDER:
        c = 0
        for n, ln in prose_lines(read(f)):
            for sent in SENT.split(clean(ln)):
                body = strip_quotes(sent).replace("QUOTE", "")
                words = re.findall(r"[A-Za-z][A-Za-z'’-]*", body)
                if len(words) > 25:
                    c += 1
                    rows.append((f, n, len(words), sent.strip()))
        counts[f] = c
    return rows, counts


def theme_counts():
    pats = {
        "lust": r"\blust", "porn": r"\bporn", "women/woman": r"\bwom[ae]n\b",
        "masturbat/MO": r"\bmasturbat|\bMO\b|\bjerk", "habit": r"\bhabit",
        "soldier/duty/fit": r"\bsoldier|\bduty\b|\bunfit\b|\bfit for\b|\bdrunk\b|\bsober",
        "Little Monster": r"Little Monster", "Big Monster": r"Big Monster",
        "wrong head": r"wrong head", "thread (can't be trusted)": r"can't control his lust can't be trusted",
    }
    rows = []
    for f in BOOK_ORDER:
        txt = " ".join(clean(l) for _, l in prose_lines(read(f)))
        rows.append((LABEL[f], len(txt.split()), {k: len(re.findall(p, txt, flags=re.I if k not in ("Little Monster", "Big Monster", "masturbat/MO") else 0)) for k, p in pats.items()}))
    return pats, rows


def repeated_phrases(n=5, min_count=4, min_files=3):
    """n-word phrases that occur min_count+ times across min_files+ files (prose only)."""
    cnt, where = Counter(), {}
    for f in BOOK_ORDER:
        txt = " ".join(clean(l) for _, l in prose_lines(read(f)))
        words = re.findall(r"[a-z']+", strip_quotes(txt).lower())
        seen = set()
        for i in range(len(words) - n + 1):
            g = " ".join(words[i:i + n])
            cnt[g] += 1
            where.setdefault(g, set()).add(LABEL[f])
    stop = re.compile(r"^(the|a|of|to|and|in|that|it|is|you|he|his|for|on|with|be|as|but|not)( |$)")
    out = [(g, c, sorted(where[g])) for g, c in cnt.items() if c >= min_count and len(where[g]) >= min_files and not re.fullmatch(r"(\w+ ?)+", g) is None]
    out.sort(key=lambda x: (-x[1], x[0]))
    # drop phrases contained in a longer reported phrase with the same count
    kept = []
    for g, c, w in out:
        if not any(g in k[0] and k[1] == c for k in kept):
            kept.append((g, c, w))
    return kept[:60]


OVERUSED = [
    "marvellous", "stop kidding yourself", "of course", "honestly", "plain", "plainly", "simply", "actually",
    "exactly", "really", "quite", "perhaps", "obviously", "trap", "chain", "pipsqueak", "willpower method",
    "isn't it marvellous", "nothing", "no such thing", "doesn't exist", "the truth", "free man", "a man who",
    "sin", "grace", "itch", "relief", "comfort", "crutch", "prop", "mope", "moping", "pity", "envy",
]


def overused_words():
    allp = []
    per = {}
    for f in BOOK_ORDER:
        txt = " ".join(clean(l) for _, l in prose_lines(read(f))).lower()
        per[LABEL[f]] = txt
        allp.append(txt)
    big = " ".join(allp)
    total = len(big.split())
    rows = []
    for w in OVERUSED:
        c = len(re.findall(r"\b" + re.escape(w) + r"\b", big))
        files = [k for k, t in per.items() if re.search(r"\b" + re.escape(w) + r"\b", t)]
        rows.append((w, c, round(c * 1000 / total, 2), len(files)))
    return total, rows


def leftovers():
    out = []
    pats = {
        "pen name / author name in book files": r"AnotherHack|Rooke|James Rooke|my name is|I'm (James|the author)",
        "EasyPeasy author credit (Hackauthor)": r"Hackauthor",
        "'hackbook' (unexplained jargon)": r"hackbook",
        "first-person author anecdote (I + past tense)": r"\bI (used to|was|went|have been|tried|once|remember|still|never needed|couldn't tell you|enjoy|bit|stole|'ve (thought|stolen|made))\b",
        "'wifey' / casual": r"\bwifey\b",
        "'sequel' (allowed only as 'not an official sequel')": r"\bsequel\b",
        "'play along' (allowed: Intro, Ch 32)": r"play along",
        "'atheist' (convention: say 'not a believer')": r"\batheist",
        "'jerking off' (use rarely, on purpose)": r"jerk(ing)? off|jerked off",
    }
    for label, p in pats.items():
        hits = []
        for f in BOOK_ORDER:
            for n, ln in prose_lines(read(f)):
                if re.search(p, strip_quotes(ln) if label.startswith("first-person") else ln):
                    hits.append(f"{LABEL[f]}:{n}")
        out.append((label, hits))
    # non-book files that expose the repo owner
    leaks = []
    for g in ("_output.yml", "_bookdown.yml", "tools/seo.py", "README.md", "site/*.js", "worker/*"):
        for path in glob.glob(os.path.join(ROOT, g)):
            for i, ln in enumerate(open(path, encoding="utf-8", errors="ignore"), 1):
                if re.search(r"IamJamesRooke|iamjamesrooke", ln):
                    leaks.append(f"{os.path.relpath(path, ROOT)}:{i}")
    # cross references
    xrefs = []
    for f in BOOK_ORDER:
        for n, ln in prose_lines(read(f)):
            for m in re.finditer(r"Chapters? (\d+)(?:[–-](\d+))?", ln):
                xrefs.append((LABEL[f], n, m.group(0), clean(ln)[max(0, m.start() - 60): m.end() + 60].replace("\n", " ")))
    # God pronoun capitalisation
    caps = {"He/His (God)": 0, "he/his (God)": 0}
    god_cap, god_low = [], []
    for f in BOOK_ORDER:
        for n, ln in prose_lines(read(f)):
            s = strip_quotes(clean(ln))
            if re.search(r"\bGod\b[^.]{0,60}\b(He|His|Him)\b|\b(He|His|Him)\b[^.]{0,30}\bGod\b", s):
                god_cap.append(f"{LABEL[f]}:{n}")
            if re.search(r"\bGod\b[^.]{0,60}\b(he|his|him)\b", s):
                god_low.append(f"{LABEL[f]}:{n}")
    # British vs American spellings
    br = Counter(); am = Counter()
    pairs = [("colour", "color"), ("favour", "favor"), ("realise", "realize"), ("recognise", "recognize"),
             ("neighbour", "neighbor"), ("labour", "labor"), ("honour", "honor"), ("organis", "organiz"),
             ("defence", "defense"), ("grey", "gray"), ("fortnight", "two weeks"), ("mum", "mom"), ("whilst", "while")]
    for f in BOOK_ORDER:
        txt = " ".join(clean(l) for _, l in prose_lines(read(f))).lower()
        for b, a in pairs:
            br[b] += len(re.findall(b, txt))
            am[a] += len(re.findall(r"\b" + a + (r"\b" if a in ("mom", "while") else ""), txt))
    return out, leaks, xrefs, (god_cap, god_low), (br, am, pairs)


def main():
    rows, counts = long_sentences()
    with open(os.path.join(OUT, "long-sentences.md"), "w", encoding="utf-8") as fh:
        fh.write("# Sentences over 25 words (quotations excluded)\n\n")
        fh.write("Generated by `tools/editorial_checks.py`. Counts per file, then the sentences.\n\n")
        fh.write("| File | Over 25 words |\n|---|---|\n")
        for f in BOOK_ORDER:
            fh.write(f"| {LABEL[f]} | {counts[f]} |\n")
        fh.write(f"| **Total** | **{sum(counts.values())}** |\n\n")
        cur = None
        for f, n, w, s in rows:
            if f != cur:
                fh.write(f"\n## {LABEL[f]}  ({f})\n\n")
                cur = f
            fh.write(f"- L{n} ({w}w): {s}\n")

    pats, theme = theme_counts()
    total, ow = overused_words()
    rep = repeated_phrases()
    with open(os.path.join(OUT, "word-use.md"), "w", encoding="utf-8") as fh:
        fh.write("# Word use across the book\n\n")
        fh.write("## Theme counts per file (prose only, quotes and blockquotes excluded)\n\n")
        keys = list(pats.keys())
        fh.write("| File | words | " + " | ".join(keys) + " |\n|---|---|" + "---|" * len(keys) + "\n")
        for lab, wc, d in theme:
            fh.write(f"| {lab} | {wc} | " + " | ".join(str(d[k]) for k in keys) + " |\n")
        fh.write(f"\n## Overused words and phrases (book total {total} words)\n\n| Word | Count | Per 1000 words | In how many files |\n|---|---|---|---|\n")
        for w, c, per, nf in sorted(ow, key=lambda r: -r[1]):
            fh.write(f"| {w} | {c} | {per} | {nf} |\n")
        fh.write("\n## Five-word phrases used 4+ times in 3+ files\n\n")
        for g, c, w in rep:
            fh.write(f"- \"{g}\" x{c} in {', '.join(w)}\n")

    out, leaks, xrefs, (gc, gl), (br, am, pairs) = leftovers()
    with open(os.path.join(OUT, "leftovers.md"), "w", encoding="utf-8") as fh:
        fh.write("# Leftovers and style flags\n\n")
        for label, hits in out:
            fh.write(f"- **{label}**: {len(hits)} hit(s) {', '.join(hits[:40])}\n")
        fh.write("\n## Files outside the chapters that name the repository owner\n\n")
        for l in leaks:
            fh.write(f"- {l}\n")
        fh.write("\n## Pronoun for God: capitalised vs lowercase (prose lines)\n\n")
        fh.write(f"- capitalised He/His/Him near 'God': {len(gc)} lines: {', '.join(gc)}\n")
        fh.write(f"- lowercase he/his/him near 'God': {len(gl)} lines: {', '.join(gl)}\n")
        fh.write("\n## British vs American spelling (prose)\n\n")
        for b, a in pairs:
            fh.write(f"- {b}: {br[b]}  |  {a}: {am[a]}\n")
        fh.write("\n## 'Chapter N' cross-references (check each against the target chapter)\n\n")
        for lab, n, ref, ctx in xrefs:
            fh.write(f"- {lab}:{n} {ref}: ...{ctx}...\n")
    print("wrote", OUT)
    print("long sentences:", sum(counts.values()), "in", sum(1 for v in counts.values() if v), "files")


if __name__ == "__main__":
    main()

# Writing brief (for every chapter)

The book: *The Easy Peasy Way to Stop Jerking Off* by AnotherHackAuthor. It is a SEQUEL to [EasyPeasy](https://easypeasymethod.org/), which is based on Allen Carr. The reader has quit porn, or wants to; the next level is removing masturbation and lust. We are writing a fast first draft; editorial passes come later.

## Sources to read for each chapter
- **EasyPeasy plain text:** `/tmp/claude-0/-home-user/f73c4488-5e98-5895-9bd4-3978678a5a69/scratchpad/epub/all.txt`. Our chapter file `NN-*.Rmd` corresponds to EasyPeasy section `ch0(NN+1)` (e.g. our 02 = their ch003). Copy each chapter's job, order, devices and rhythm. **Never copy its sentences.**
- **The outline:** `OUTLINE.md`, with the global rules and the entry for the chapter.
- **Research:** `research/nofap-movement.md` (with its "Ideas for chapters" map), `research/more-sources.md` (if present), `research/transcripts/*.md` (FitXFearless, aka Bismarck Ebiweh), `research/ch00-introduction.md`.
- **Voice reference:** `index.Rmd` and `01-the-easy-method.Rmd` (James loved the intro; match it).

## Rules
1. **Voice:** EasyPeasy's. Second person, confident, warm, repetitive, short paragraphs, slogans in caps, the odd joke. Use "masturbation", "MO", "the habit" and "jerking off" interchangeably.
2. **Faith:** a Christian scaffold, not preachy, helping ANYONE. One or two verses per chapter, in World English Bible (WEB) wording you're sure of. The Bible is the only religious text quoted at length; Christian writers (C.S. Lewis, Augustine, Piper and others) may be quoted briefly and attributed. Occasional "if you're an atheist, play along".
3. **Audience:** men; mastering lust; the self-control thread: "A man who can't control his lust can't be trusted."
4. **Claims:** harm to drive and so on is stated as conviction and testimony, never as medical findings. No invented studies, statistics, quotes or sources. Keep the recurring metaphors: Little Monster, Big Monster.
5. **Quotes:** only from the research files, verbatim, short, anonymised for forum users ("a man on a NoFap forum"). End each chapter file with `<!-- SOURCES: quote — source link -->`.
6. **Keep EasyPeasy's rules:** carry on as normal until the end of the book; no cutting down; no substitutes. The final step is a prayer of confession, not a final session. No Karezza. Semen retention is offered as "try it and see" in the First Weeks chapter.
7. **Length:** roughly EasyPeasy's chapter length, up to 20% more.
8. **Format:** R Markdown for Bookdown. Start the file with `# Chapter Title`; sub-headings use `## Heading {-}`.
9. **Originality check:** `python3 /tmp/claude-0/-home-user/f73c4488-5e98-5895-9bd4-3978678a5a69/scratchpad/overlap.py <files>` must show 0 shared 7-word runs (Bible quotes excepted). Reword until it does.

## Revision conventions (added 2026-11-14)

- **Everything lives on `main`.** No branches and no pull requests. James edits the `.Rmd` files directly in VS Code.
- **James's notes.** He leaves a note as an HTML comment on its own line (ideally `<!-- NOTE: ... -->`), next to the paragraph it refers to. When he says a chapter's notes are in: pull main, apply every note in that chapter in one pass, remove the note comments, keep his direct edits, commit to main, and report briefly.
- **Word choice (James, 2026-11-14).** Use "masturbation" as the normal word. "Jerking off" is more vulgar: use it rarely and on purpose, for bluntness or shock. The title keeps it.
- **"If you're an atheist, play along."** Use it once or twice in the whole book, not in every chapter. It is kept in the Introduction, the final step (Chapter 27) and the blessing (Chapter 32).
- **Source names.** Creators such as FitXFearless are described in the body ("one coach") and named only in the SOURCES comment and on the attribution page.
- **Quotes.** A quote that cannot be checked against its source becomes a paraphrase, with a note in SOURCES saying why.

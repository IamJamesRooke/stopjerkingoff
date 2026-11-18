# Writing brief (for every chapter)

The book: *Stop Jerking Off: The Easy Peasy Guide to Quitting Masturbation and Conquering Lust*. The author is ANONYMOUS (James, 2026-11-17: no pen name anywhere, and no references to the author's identity; "this isn't about me"). It is a SPIRITUAL SUCCESSOR to [EasyPeasy](https://easypeasymethod.org/) (James, 2026-11-15: never call it a sequel), which is based on Allen Carr. The reader has quit porn, or wants to; the next level is removing masturbation and lust. We are writing a fast first draft; editorial passes come later.

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
- **"If you're an atheist, play along."** Use it once or twice in the whole book, not in every chapter. It is kept in the Introduction and the blessing (Chapter 32). Elsewhere say "if you're not a believer" and give the unbeliever something to do.
- **Source names.** Creators such as FitXFearless are described in the body ("one coach") and named only in the SOURCES comment and on the attribution page.
- **Quotes.** A quote that cannot be checked against its source becomes a paraphrase, with a note in SOURCES saying why.

## Scope and plain-language rules (added 2026-11-17, from James)

**Scope.** The book is about conquering lust, not only masturbation. Lust has
three faces: porn, the hand, and the bad decisions a man makes around women
("thinking with the wrong head"). Porn is fully in scope; EasyPeasy is still
credited and recommended, but readers are not sent away to it.

- "The habit" means masturbation, with or without porn. When a claim is true of
  lust in general, say "lust". Leave passages about the act itself (the body,
  sleep, the first weeks) as they are.
- Lust is not desire. Noticing beauty and wanting a wife are good. Lust is
  desire turned into taking. Keep that distinction near any wider claim.
- The frame is "fit for service": a man ruled by lust is a soldier who shows
  up for duty drunk. He is loved and he is unfit. It opens the Introduction and
  pays off in the chapter "Fit for Service". Never let "unfit" read as
  "unloved".
- "Simping" appears once, in the Introduction, with a plain explanation.
  Elsewhere describe the thing in ordinary words. Write about women with
  respect: the fault is the man's thirst, not the woman.
- "Carry on as normal until the last page" is about private habits. It is never
  permission to hurt someone (an affair, using a woman, anything illegal).

**Plain language.**

- One idea per sentence. Split any sentence over about 25 words unless it is a
  quotation or a verse.
- Prefer the everyday word. Rewrite an awkward sentence; don't patch it.
- Never change Bible verses or quoted words.
- Check each chapter with the long-sentence script (sentences over 25 words,
  quotations excluded) before and after editing.

## Standing rule: it must sound good read aloud (James, 2026-11-18)

There will be a definitive audiobook. Every line must sound good when it is heard, not only when it is read.

- Read each paragraph aloud in your head before it goes in. If a listener would lose the thread, split or reorder it.
- No brackets for asides. Say it as a sentence or cut it.
- Put a Scripture reference into the sentence ("In Romans 8:1 Paul says...") where it reads naturally. A trailing reference in brackets is fine for a closing verse.
- Quotations with typos, missing punctuation, slang shorthand or symbols become paraphrases, with the source kept in SOURCES.
- Avoid three sentences or paragraphs in a row that begin with the same words, unless the repetition is on purpose.
- Spell out what a narrator can't say: no "/" alternatives, no "&", numbers that read cleanly.
- Capitals are for one short slogan at a time, never for a run of sentences.

## Standing rule: American English, plain enough for a non-native speaker (James, 2026-11-18)

- American spelling throughout the book and the site text: license, realize, behavior, center, gray, toward, counselor, marvelous.
- American wording in place of British: apartment, vacation, movie, coworker, sneakers, highway, schedule, two weeks, fight (not row), call (not ring), sick (not ill), around (not round), right away.
- Idioms must be ones a non-native English speaker can follow. This also keeps the later Spanish edition easy to translate. When in doubt, say it plainly.
- Leave direct quotations exactly as their authors wrote them, British spelling included (for example "I harboured a wrong notion" in Chapter 15). WEB Scripture stays verbatim.
- Chapter 18 is titled "Can I Compartmentalize?" but keeps its old address, can-i-compartmentalise.html, through an explicit heading ID. Do not remove the ID.
- "Flat" for the low mood after the act is kept as a running image. "Flat" for a home is "apartment".

## Standing rule: every reference gets a line of context (James, 2026-11-18)

Most readers have not read the Bible or the books this one draws on. Whenever a person, a book or a story is mentioned, say in a few plain words who or what it is, the first time it appears in a chapter that leans on it.

- Bible people and stories: one clause or sentence. "David was Israel's greatest king." "Jesus told a story about a son who took his inheritance early."
- Books and authors: say what the book is. *The Screwtape Letters* is a set of letters from a senior devil coaching a junior one.
- A verse at the top of a chapter can be pointed to as "the verse that opens this chapter", so the listener knows where the name came from.
- Keep it short and good read aloud. One sentence is usually enough. Never assume the reader is a Christian.

# Writing brief (for every chapter)

The book: *Stop Jerking Off: The Easy Peasy Guide to Quitting Masturbation and Conquering Lust*. The author is ANONYMOUS (James, 2026-11-17: no pen name anywhere, and no references to the author's identity; "this isn't about me"). It is INSPIRED BY (James, 2026-11-18: not "spiritual successor", and never called free) [EasyPeasy](https://easypeasymethod.org/) (James, 2026-11-15: never call it a sequel), which is based on Allen Carr. The reader has quit porn, or wants to; the next level is removing masturbation and lust. We are writing a fast first draft; editorial passes come later.

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

## Standing rule: a key line may stand alone (James, 2026-11-18)

A one-line paragraph, even a sentence fragment such as "Not one.", is welcome where it carries the point. It gives the narrator a pause and varies the length of the paragraphs.

- Use it sparingly: about once or twice a chapter.
- Only on the line that carries the point of the passage. Never on a line of setup or a joke.
- Do not stack two of them back to back.

### Never send the reader back or forward (James, 2026-11-18)

Never tell the reader to go and find something: no "read the verse at the head of the chapter again", "see above", "below", "scroll up". Nobody scrolls back, and a listener can't. Restate the line in place, in a few words or in full. Naming a chapter in passing ("Chapter 8 described this") is fine when the sentence still works without looking it up. Advice to re-read the book or a chapter after a slip is part of the method and stays.

### Chapter numbers (2026-11-19)

James split the old Chapter 8. The stories are now Chapter 9, "A City Without Walls" (`09-a-city-without-walls.Rmd`), and every later chapter and file moved up by one. Our file `NN` now matches EasyPeasy section `ch0(NN+1)` only up to Chapter 8; from Chapter 10 on it matches `ch0(NN)`. Page addresses did not change, because they come from the headings.

## Standing rule: "partner", not "wife", for the reader's own woman (James, 2026-11-19)

We don't know whether the reader is married. In general lines about the
woman in his life, write "partner" ("short with his partner", "his partner is
asleep in the next room"). Keep "wife" and "husband" where the line is about
marriage itself: Bible stories, quotations and testimonies, "wanting a wife",
"sex with your wife is the meal", the married-man section, the "If you're
married" lines, "To wives", and "the woman you'll marry".

## Standing rule: no "user" (James, 2026-11-19)

"User" and "non-user" are drug and software words left over from the smoking
book. Write "a man in the trap", "hooked", "the man who does it daily", "a man
who's free". Chapter 14 is "Every Man in the Trap" and Chapter 31 is "For the
People Beside Him"; both keep their old page addresses through heading IDs.

## Standing rule: vivid archetypal stories (James, 2026-11-19)

"Absolute truth isn't the point. The point is motivating men to change with
archetypal stories that most men can relate to." An illustration may be
invented or filled out with detail (a setting, what was said, what he told
himself), as long as it is generic enough that any man can see himself in it.
Frame it as an illustration: "There's a man you may recognize", "Picture a
man". Never present an invented story as a testimony, never put invented words
in a real or quoted person's mouth, and never invent facts, studies or
Scripture. Real testimonies stay as their authors wrote them. Note in the
chapter's ADDED comment which parts are invented.

## Standing rule: no ellipses (James, 2026-11-19)

No "…" or "..." in the book. End the sentence, or finish the thought. A
character's line doesn't trail off. Quote whole Bible sentences rather than
marking an omission.

## Standing rule: church references only where they're needed (James, 2026-11-19)

"We don't have to add references to the church every moment of the book. We
want this book to be attractive to non-Christian readers." Don't reach for
"in church", "on Sunday" or "your pastor" as a reflex in illustrations and
stories. Use everyday pictures any man shares. Keep the Christian material
where it carries the argument: Scripture, grace, prayer, the Christian
sections.

## Standing rule: evergreen (James, 2026-11-19)

A man should be able to read this book in a hundred years and think it reads
surprisingly well. Tie every point to human nature, not to the current technology.

- No helpline names, phone numbers or websites. Tell the reader to see a doctor, a
  counselor, or call his local emergency number. Keeping contacts current is not our job.
- The only web addresses in the visible text are the book's own home and the CC BY-SA
  credit to EasyPeasy. Source links stay in the hidden SOURCES comments.
- No brand, site or app names as the point of a sentence. Say "the feed", "a dating
  app", "the biggest porn site", "the card companies". NoFap is the one named movement,
  defined once in the Introduction.
- Facts that will date are told as history, with their year ("In 2020 ...", "in the
  early 2020s"). Never "recently", "the newest", "these days", "this one is new".
- Slang is dated on purpose ("the slang of the 2020s calls this simping") and then
  tied to the old thing it names.
- "Phone", "screen", "feed" and "scroll" are fine. They are the furniture of the
  reader's life and will still be understood.

## Standing rule: quote only when the quote earns its place (James, 2026-11-19)

Quote or cite someone only when it adds real value: a vivid line the book couldn't
say better, an authority the point needs (a doctor on medicine, a psychiatrist on
relapse), or a true testimony. Otherwise cut the attribution and let the book say it
in its own voice. The source stays in the chapter's SOURCES comment.

- Never "the same coach", "the pastor from earlier", "the writer I quoted a moment
  ago". The reader, and above all the listener, won't remember who that was. Where a
  quote stays, identify the speaker in place, briefly, every time.
- A paraphrase with an attribution ("One coach describes...", "A pastor says the same")
  is nearly always filler. Say the thing.
- No stacking: one voice per point.

## Standing rule, strengthened: no cross-references at all (James, 2026-11-19)

Nobody goes back to check a reference, and a listener can't. A book has no hyperlinks.
Whenever a point from elsewhere is needed, say it again, here, in a sentence.

- Never write "Chapter 7", "two chapters ago", "the last chapter", "as you saw",
  "you met him earlier", "the Introduction said", "I said", "comes up later",
  "Chapter 29 covers it". Before pushing, search for: chapter, earlier, above, below,
  go back, you saw, you met, I said, later, the Introduction.
- A quote or person used a second time is introduced again in place, in a few words.
- Allowed: a plain promise of what is coming next ("the next chapter sets out the
  advantages"), the named things the book owns (the final step, If You Slip, the
  Little Monster), "the verse that opens this chapter", and advice to read the book
  again after a fall. The FAQ may link to chapters, because it is a web page.

## Responsibility without pretending (James, 2026-11-19)

The book asks the man to take responsibility because his own conduct is the thing he can
control. It does not pretend that women are angels. Women can manipulate, use sex as a
lever and do wrong, and the book may say so plainly, in one sentence, without contempt.
Then it returns to what the man can change. Never excuse her to flatter the reader, and
never blame her to excuse him.

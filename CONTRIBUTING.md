# Contributing

Thank you for helping make this book better. Every chapter is a plain Markdown file, so you can suggest a change without installing anything.

## Ways to help

- **Fix a typo or a clumsy sentence.** Open the chapter in [`chapters/`](chapters/), click the pencil icon on GitHub, make the change and choose **Propose changes**. GitHub forks the repository and opens a pull request for you.
- **Suggest something bigger.** A new idea, a section that didn't work for you, a fact that looks wrong: [open an issue](../../issues/new/choose) first, so it can be discussed before anyone rewrites a chapter.
- **Share what happened to you.** If the book helped, or didn't, an issue using the "Reader feedback" template is welcome. Leave out anything that could identify you or anyone else.
- **Translate it.** Translations are planned once the English text is final. Open an issue before you start, so work isn't duplicated.

## Where things are

- The book: `chapters/`, one file per chapter. The file number gives the reading order. `00-introduction.md` is the Introduction.
- Website-only pages (FAQ, About, "Why this book"): `pages/`.
- The chapter order for the website, PDF and EPUB: `_bookdown.yml`. A new chapter has to be added to all three lists there.

You don't need to build the book to suggest an edit. If you want to see your change rendered, the [README](README.md#build-it-yourself) explains how.

## How the book is written

Please keep these in mind. A change that breaks them will be asked to change, however good the writing.

1. **It is read aloud.** An audiobook is made from this text, so every sentence must sound natural spoken. No ellipses, no "see above", no lists that only work on a page.
2. **Plain words, short sentences.** Second person, warm and confident. Write for a tired man at midnight, not for a reviewer.
3. **It should still read well in a hundred years.** No phone numbers, website addresses, trendy slang or "these days". A dated fact carries its year.
4. **No invented facts.** Effects on the body are stated as experience and testimony, not as medical findings. No made-up studies, statistics or quotes. A quotation must be short, verbatim and sourced. Put the source in an HTML comment at the end of the chapter: `<!-- SOURCES: "quote" — link -->`.
5. **Name people only when it adds something:** a vivid line, needed authority or a real testimony. Forum users stay anonymous ("a man on a recovery forum").
6. **The method's core lines stay.** Read to the end before stopping; no cutting down; no substitutes; no willpower campaign; "just once" does not exist. Edits that soften these will not be merged.
7. **Faith is the foundation, not a gate.** Bible quotations use the World English Bible. The book must work for a reader who doesn't believe.
8. **Men take responsibility for what they can control.** The book doesn't blame women, and it doesn't pretend nobody else ever does wrong.
9. **American English** spelling and punctuation, with curly quotes left to the build.
10. **The book is anonymous.** Don't add an author name, a byline or personal details, yours included.

### Markdown conventions

- Each chapter file starts with `# Chapter Title`.
- Section headings inside a chapter are `## Heading {-}` (the `{-}` keeps them unnumbered).
- An epigraph is a block quote (`> ...`) placed straight after the chapter title.
- Notes for editors go in HTML comments: `<!-- NOTE: ... -->`. They never appear in the book.

## Pull requests

- Keep each pull request to one topic, so it can be reviewed and merged quickly.
- Say in a sentence or two what you changed and why.
- The editors may reword a change before merging it, to keep one voice across the book. Not every suggestion will be taken, and that is no judgment on you.

## License of contributions

The book is released under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). By opening a pull request or submitting text in an issue, you agree that your contribution is released under the same license, and that you have the right to give it. Code changes are released under the repository's [GPLv3 license](LICENSE).

## Conduct

Be kind and be direct. This book deals with shame, and many people who read this repository are struggling. Mockery, harassment, sexual content and personal attacks will be removed, and repeat offenders blocked.

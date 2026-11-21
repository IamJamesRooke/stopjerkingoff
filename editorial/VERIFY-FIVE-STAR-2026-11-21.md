# Cold-read verification: book-five-star.txt

Read in full, in order (all 61 chapters, afterword, appendix, attribution). A script also checked for doubled words and for any sentence over 45 characters appearing twice: none found.

**Headline: no restructuring break is severe.** Every chapter-ending hook is met by the next opening. Every item on the watch list is introduced before it is used (table at the end). What remains is one count mismatch, a few places where the text forgets whether the reader has decided yet, and small polish items.

## Medium

**M1. Count mismatch: "Four men" after five were described**
- FILE: `chapters/14d-the-chase.md` (ch 35)
- Quote: `Four men, then: the one at the party, the one who waits, the one who swipes and the one who can't let go.`
- Problem: the chapter has five portraits: the party man, "The man who waits", "The man who swipes", "The one girl" (the obsessive texter) and "If she has said no" (the man still writing). "Can't let go" covers only one of the last two.
- Fix: `Five men, then: the one at the party, the one who waits, the one who swipes, the one who is texting a picture in his head and the one who can't let go.`

**M2. Post-decision chapter talks to a man who has not started**
- FILE: `chapters/29-feedback.md` (ch 57)
- Quotes: `Two keep him from starting, and two trip him once he has.` and `Refusing to try is plain foolishness. What are you protecting by not trying?`
- Problem: by ch 55 the reader "has said his No", and ch 56 ends "That is the method, start to finish." Sections 1 and 2 then address a man who has not yet tried.
- Fix: reframe both as fears that come back afterward. Opening: `Two are fears that can come back and make him doubt, and two are mistakes in carrying it out.` Section 1: `Failing is no disgrace. If the fear of failing comes back after you have decided, ask what it is protecting. Nothing. A man who falls is exactly where he was the day before he decided, and he gets up.`

**M3. "Read on" at the Final Step points the wrong way**
- FILE: `chapters/28-the-final-step.md` (ch 54)
- Quote: `If so, read on until that belief is gone.`
- Problem: everything after this page assumes the decision is made ("You have said your No"). A man who still believes will not find the argument by reading on.
- Fix: `If so, go back to the chapter that deals with it, and come back here when that belief is gone.`

**M4. When to stop: "the day you finish this book" vs the Final Step at ch 54 of 61**
- FILE: `chapters/17-timing.md` (ch 41)
- Quotes: `It asks you to finish reading, and then stop, whatever week it is.` / `So the time is the day you finish this book` / `Look at the three weeks after you expect to finish the book.`
- Problem: the same chapter says "You stop at the final step, near the end." The decision comes seven chapters before the book ends.
- Fix: `It asks you to read as far as the final step, and then stop, whatever week it is.` / `So the time is the day you reach the final step` / `Look at the three weeks after you expect to reach it.`

**M5. "Lust" used as the subject inside the habit-only half**
- FILES: `chapters/09-a-city-without-walls.md` (ch 22, last paragraph) and `chapters/10-advantages-of-jerking-off.md` (ch 23 title)
- Quotes: `You've heard at length what lust costs a man` / `the advantages of lust.` / `# 23. Advantages of Lust`
- Problem: chapters 16 to 22 counted what "the habit" costs. By the book's own vocabulary "lust" is the wider appetite, not argued until ch 31. A listener cannot tell whether the subject has widened.
- Fix: `You've heard at length what the habit costs a man ... the advantages of the habit.` and `# 23. Advantages of the Habit`. ("A man who can't control his lust can't be trusted" in ch 21 is fine and is quoted back in ch 45.)

## Low

**L1. Same section heading in two chapters**
- FILES: `chapters/16-a-secret-habit.md` (ch 40) and `chapters/24-will-it-be-harder-for-me.md` (ch 49)
- Quote: `## The man at the front of the church {-}` (both)
- Problem: two sections with one title and overlapping content (the church volunteer with a secret; the pastor with a secret).
- Fix: rename the ch 49 one `## The man who leads the church {-}` and open it `You met the man at the front of the church. Harder still, you'd think, is the man who leads it.`

**L2. "The other hard-looking case" after three cases**
- FILE: `chapters/24-will-it-be-harder-for-me.md` (ch 49)
- Quote: `The other hard-looking case is boredom mixed with stress.`
- Problem: "the other" implies one earlier case; three came before. Looks like a remnant of a cut.
- Fix: `One more hard-looking case is boredom mixed with stress.`

**L3. The caller changes identity**
- FILE: `chapters/22a-whose-voice-is-that.md` (ch 47)
- Quote: `Now treat him as the caller he is.`
- Problem: "him" here is the Big Monster (the voice). In ch 28 and 29 the caller is the Little Monster, and "The caller himself can't speak ... The old lie does his talking for him."
- Fix: `Now treat it as what it is, the caller's message.`

**L4. Unsupported back-reference**
- FILE: `chapters/31-advice-to-non-users.md` (Afterword, "To parents")
- Quote: `Several of the men quoted in this book started at ten.`
- Problem: no man in the text as it stands says he started at ten (ages given are twelve, twelve, thirteen, fourteen). The quotes were probably cut.
- Fix: `Several of the men quoted in this book started at twelve, and many men start younger.`

**L5. The marriage rule is stated one chapter early**
- FILE: `chapters/14e-the-collector-and-the-customer.md` (ch 37)
- Quote: `Suppose you had lived by that rule: sex only with the woman you have promised to keep.`
- Problem: design says the rule is first stated in ch 38. It is framed as a thought experiment, so it may be intended. If not:
- Fix: `Suppose you had only ever gone to bed with a woman you meant to keep.` and, two paragraphs on, `Of the men who live the other way, how many would you trust with your sister?`

**L6. People introduced as new a second time**
- `chapters/15b-you-would-if-you-could.md` (ch 33): `C.S. Lewis saw all this. He called it a harem of imaginary brides` – the phrase was already given in ch 15. Fix: `You have already met Lewis's harem of imaginary brides. He also saw what the harem does to a man.`
- The same preacher arrives three times as a stranger: `A preacher who was bound by this habit for years` (ch 6, `03-the-flesh.md`), `One preacher, who was bound by masturbation for years himself` (ch 10, `04-the-worlds-lies.md`), `One man who was bound by the habit for years` (ch 51, `26-should-i-avoid-temptation.md`). Fix for ch 10: `The preacher who was bound by this for years answers in nine words`.
- `chapters/08-what-its-doing-to-you.md` (ch 18): `The same coach masturbated daily for years himself` – the coach was last heard a chapter earlier. Fix: `The coach who spoke of ideas with zero execution masturbated daily for years himself`.

**L7. "Two instructions" collision**
- FILE: `chapters/25-substitutes.md` (ch 50)
- Quote: `He gives two instructions. The first is *flee*`
- Problem: "the two instructions" is the method's fixed term (decide, rejoice), used one chapter earlier.
- Fix: `He gives two commands.`

**L8. "The bell" used before it is set up**
- FILE: `chapters/22-the-first-weeks.md` (ch 46)
- Quote: `Monday he gets into bed and the bell rings on schedule.`
- Problem: the bell image is only explained three sections later ("the places themselves now ring the bell"). The couch-man week was probably moved above it.
- Fix: `Monday he gets into bed and the old cue goes off on schedule, like a bell.`

**L9. Repeats worth a decision (not move leftovers)**
- `The rule is strict, and the grace is real.` appears in ch 55 (`28a-let-it-ring.md`) and again in ch 58 (`29b-if-you-slip.md`). Keep one, or make ch 58 `As you were told: the rule is strict, and the grace is real.`
- The couch man's phone "lying face up" pays off in ch 52 (`27-the-moment-of-revelation.md`) and again in ch 61 (`33-now.md`). The second lands softer for it. Consider keeping only the ending.
- `None of this is new.` opens a story three times (ch 21, 29, 36).

**L10. Typos and housekeeping**
- `chapters/01-the-easy-method.md` (ch 2): `*Easy Way to Stop Smoking*` – the Appendix and Attribution give `*The Easy Way to Stop Smoking*`.
- Stale anchors that no longer match headings: ch 32 "A Scroll Isn't Porn" carries `{#fantasy-and-the-thought-life}` (fantasy is now ch 33); ch 11 "The Lies About Porn" carries `{#the-lies-about-porn-and-about-women}`; ch 1 "The Button" carries `{#a-warning}`. Any internal link to these lands on the wrong topic.
- No doubled words and no broken Markdown found.

## Categories that are clean

- **Broken joins:** clean. All 60 chapter-to-chapter hooks are met. Only L2 is a within-chapter remnant.
- **Duplicates from moves:** clean. No paragraph or sentence appears twice verbatim.
- **Counts:** all others check (three questions, three things tonight, five points, four instructions, four brakes, four things the secret does, four not-a-slip, three badges, four ways it goes wrong, ten rules, four verses, two instructions).
- **Early arrivals:** clean apart from M5 and L5. Mentions of women before ch 31 are passing (intro, ch 3, ch 15 "After the date", the ch 30 line-up).
- **Stopping instructions:** consistent from intro to ch 53 ("no vow, stay stopped if stopped, one decision at the final step"), apart from M2 to M4.

## Watch-list check

| Item | First introduced | Later uses | Status |
|---|---|---|---|
| The button | Intro / ch 1 | ch 5 (nightstand), ch 61 | OK |
| Paul | ch 2, glossed | throughout | OK |
| C.S. Lewis | ch 6, glossed | 8, 15, 16, 18, 33, 40 | OK (L6) |
| Big Monster | ch 10 | from ch 13 | OK, not used earlier |
| Dr. Kanojia | ch 13, full name | "the same psychiatrist" ch 14; 19, 45, 46, 48 | OK |
| David | ch 14 brief, ch 20 | full story ch 22; 29, 53 | OK |
| Peter | ch 26, glossed | 40, 53, 59 | OK |
| de Becker, four instructions | ch 28 | 29, 35, 47, 55, 60 | OK |
| Telephone / caller | ch 28–29 | 46, 48, 55 | OK (L3) |
| Gift-or-hit test | ch 31 | 32, 35, 37, 38, 39, 57 | OK |
| "Thinking with the wrong head" | Intro | ch 35 | OK |
| The lever | ch 36 | ch 36 only | OK |
| Samson, Ahab | ch 36 | ch 36 only | OK |
| The five ways | ch 38 | 45, 61 | OK |
| The couch man | ch 40 | 45, 46, 52, 61 | OK |
| The ship | ch 59 ("one last picture") | — | OK |

## Overall impression as a reader

- It moves. Chapters 1 to 12 and the room-by-room run from 31 to 39 pull hardest; the squatter changing rooms is a real engine.
- It drags a little in two places: the cost chapters 17 to 20, which make the same point four ways, and 46 to 52, where "don't test", "don't wait" and "don't mope" recur across seven chapters before the decision.
- The ending lands. Chapter 53 sets up 54 well, the prayer is plain, and the button in "One last look" is the best callback in the book. Chapter 57 sitting after the decision (M2) is the one thing that lets air out.

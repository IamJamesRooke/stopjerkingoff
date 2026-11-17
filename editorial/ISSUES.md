# Whole-book issues list

Read of main at commit 3416cf4, 2026-11-17. No chapter text was changed. Companion files: `BIBLE.md` (what each chapter does), `checks/` (script output: long sentences, word use, leftovers; regenerate with `python3 tools/editorial_checks.py`).

Severity: **H** = fix before the book goes wider (structure, promise, safety, privacy). **M** = real reader-facing flaw. **L** = polish. IDs are stable so the Author can tick them off. "Ch" numbers follow the book; "26b" is Fit for Service.

## Status after the cut and polish pass (2026-11-17)

The book was cut from about 70,300 to about 49,700 words following `READER-REPORT.md`. Many issues below (B4 repetition, B12, 0.3, 13.2, the long-sentence list) were settled by the cuts. See section 0 of `BIBLE.md` for what each chapter now holds. Long sentences by the script: 32.

## Status after the coherence fix pass (2026-11-17)

Three batches, one pass each (commits "Coherence pass, batch 1/2/3"). Long sentences by the script: 94 before, 55 after; what is left is almost all quotation joins that the splitter can't see.

- **Fixed:** B1 (soldier threaded through 3, 8, 10, 12, 13, 20, 21, 26, 28, 28b, 31 and closed in 32), B2 (three faces named in 6, 10, 12, 15, 16, 17, 18, 20, 21, 23, 29), B5 (the vow/decision line in Ch 1, 20, 25, 31), B6, B7 (Ch 30 is now only for the people around him), B8 (slip guidance lives in the new unnumbered chapter "If You Slip", 28b), B9 (all three references), B10 (Romans 8:1), B11, B17, and chapter items 0.1, 3.1, 3.2, 4.1, 6.1, 6.3, 7.1, 8.1, 8.2, 8.3, 10.1, 10.2, 11.1, 12.1, 13.1, 13.3, 14.1, 14.2, 15.1, 16.1, 17.1, 18.1, 18.2, 19.1, 19.2, 20.1, 20.2, 21.1, 22.1, 23.1, 24.1, 24.2, 25.1, 26.1, 26.2, 26.b.2, 26.b.3, 27.1, 27.2, 28.1, 28.2, 28.3, 30.1, 30.2, 30.3, 30.4, 31.1, 32.1, 33.1, W.1, W.2.
- **Partly fixed:** B4 (the ration week, the marriage incentive, Dobson, both Lewis lines, the chain line and the wet-dream answer now have one home; the deliberate refrains and the instruction lists stay), B13, B14 (NoFap and semen retention glossed; "hackbook" gone), B15 ("cannot fail" and "fail far more often" reworded), 32.2 and W.3 (contact route is the site, no address).
- **Not done (polish, or James's call):** B3 remainder (tool files), B12 overused words, 0.3 (Intro length), 3.3, 13.2 (Ch 13 length, trimmed only a little), 22.2.

## A. Book-wide issues

- **B1 [H] The "fit for service" soldier is not threaded.** It opens the Intro, then is almost absent for 25 chapters (script count of soldier/duty/unfit/drunk/sober words: Ch 1-2 none; 3, 5, 13, 23 one passing word each; the rest zero), returns fully in 26b, gets one phrase in the Ch 27 prayer, and is not closed in Ch 32 (it says only "back in the fight"). The Intro promises it "comes back near the end", and the project brief says it runs through the book. Fix: one or two sentences in the opening or closing of about eight chapters (3, 8, 12, 20, 21, 26, 28, 32), and a one-line close in Ch 32.
- **B2 [H] Masturbation-only framing survives in the middle.** Prose counts of "lust / porn / women": Ch 10 (1/3/0), 12 (1/0/0), 15 (0/0/0), 16 (0/2/0), 17 (0/0/0), 21 (0/1/1), 22 (0/0/1), 26 (1/1/0), 29 (0/0/2). Worst of all, **Ch 20, the chapter that holds the two instructions, never names lust, porn or women** ("Decide that you will never do it again", and the "last time" story is about the hand). The prayer in Ch 27 and the Introduction cover all three faces; the chapters between do not. Fix: restate the three faces in each chapter's first or last paragraph and give one example per face. Leave passages about the act itself (body, sleep, first weeks) as they are.
- **B3 [H] The site files name the repository owner.** The chapter text is clean (no author name, no pen name; "Hackauthor²" is EasyPeasy's credit). But the published site carries `IamJamesRooke` in `_output.yml:14` (footer "Source repository" link) and `_bookdown.yml:6` (edit link on every page), and the same name sits in `tools/seo.py` (2 places), `worker/README.md:13` and `worker/feedback-worker.js` (2 places). That is a real name on an "anonymous" book. Decision for James: move the repo to a neutral account or drop the footer and edit links. Not changed.
- **B4 [M] Repeated stories and points.** Each should keep one home and a short callback elsewhere.
  - The Saturdays-only ration man: Ch 11 and Ch 13 ("A week in the life of a ration") make the same argument.
  - "I'll stop when I'm married": Ch 13, Ch 16 (list), Ch 19 (#4).
  - Dobson on carrying the habit into marriage: near-verbatim in Ch 13 and Ch 19 (also Ch 4, Ch 30).
  - Lewis "He made the pleasures..." verbatim in Ch 3 and Ch 6. Lewis "prison of himself ... harem of imaginary brides" verbatim in Ch 5 and Ch 14 (Ch 14 says "you've already met one line", then repeats it).
  - "Go back to the week before you started; would you start?" and "not one wishes it on his son": Ch 2, 4, 12, 17, 20, 27, 28.
  - Augustine's "only not yet": Ch 2, 10, 11, 16, 32 (the arc is good; the repeated line is the problem).
  - "Chain, each link forged by the one before": near-identical wording in Ch 7 and Ch 12 (also 8, 11).
  - Wet dreams: Ch 21 in full, Ch 28 again, FAQ. Edging: Ch 11 and Ch 24.
  - "This book isn't about your body": Intro, Ch 4, Ch 8 (bold).
  - Pass-it-on asks: Intro, 19, 21, 27, 29, 30, 31, 32, FAQ, Why This Book Exists. The industry paragraph appears in Ch 30 and Ch 32.
  - Five instruction lists: Ch 12 (3 things), 20 (5 things), 27 (5 conditions), 28 (7-point checklist), 30 (5 final warnings), 31 (11 instructions).
  - Epithets repeat as formulas: "a man who now teaches other men about this" x5 (Ch 3, 5, 10, 12, 20), "a psychiatrist who treats porn addiction" in four chapters, "a man on the NoFap forum, ninety days out" in Ch 6, 8, 21, "the verse that opens this chapter" x4. Full description once, then "the psychiatrist".
- **B5 [M] "No vows, no gimmicks, carry on" collides with later practical rules.** Intro: "Make no vows" and "No apps... no locked boxes". Then Ch 20 "Decide that you will never do it again", Ch 25 (charge the phone in the kitchen, delete the folder, get a roommate), Ch 27 (the prayer is a vow), Ch 28 ("You've made your vow. Keep it." and "Change nothing in your life"), Ch 31 #7 "Stop now". Each is defensible, but nowhere is the line drawn: a *willpower vow before understanding* is out; a *decision at the end with a prayer* is in; sensible phone hygiene is not a "gimmick" but a stupid-thing-avoided. Fix: one clear sentence in Ch 1 (and echo in Ch 25 and Ch 31).
- **B6 [M] Intro promises what Ch 1 does not deliver.** The Intro says Ch 1 explains "why this is not permission to sin". Ch 1 gives the caution about hurting others and says "Nobody is ordering you to do anything", but never answers the Christian objection ("You've just told me it's a sin, and now you're telling me to keep going?") in plain terms. Also James's open tone question from DRAFT-NOTES.
- **B7 [H] Chapter 30 is two chapters.** It is about 4,250 prose words and mixes audiences: the man's circle (getting him to read, wives, parents, pastors, a note on women) and the man himself (tell her?, Slipping, Wanting it to hurt, The bully, the pebble parody, porn and sex, where we leave EasyPeasy, Help end the silence, Final warning). The second half duplicates Ch 28 and Ch 32. Fix: keep Ch 30 for the people around him; move or cut the rest (see B8).
- **B8 [M] Slip guidance sits in three places at different strictness.** Ch 12/22/27 say "not once, for any reason"; Ch 28 ("I fell. Am I back to zero?") gives confess, refuse the second one, find the instruction; Ch 30 "Slipping" repeats all of it and adds more. Fix: one home (Ch 28), a pointer in Ch 30, and one sentence in Ch 27 that the rule is strict and the grace is real.
- **B9 [M] Cross-reference errors** (every other "Chapter N" reference, about 60, checked out):
  - Ch 24: "the tug-of-war from Chapter 11" (the tug-of-war is Ch 10; Ch 8 has the rope).
  - Ch 26: "Chapter 21 said ... the worst of the reminders are over in a few days". Ch 21 gives no day figures; the "five days" first appears in Ch 26.
  - Ch 28: the checklist "closes this chapter", but "More questions" follows it.
- **B10 [M] Scripture not verbatim.** `faq.Rmd` (line 27) and `why-this-book.Rmd` (line 37) quote Romans 8:1 as "no condemnation **for** those"; the book's WEB text is "**to** those" (Intro, Ch 8, Ch 20). **Open: Psalm 4:8** (Ch 5) follows ebible.org, "for you alone, Yahweh"; an older WEB reads "for you, Yahweh alone". Pick an edition and name it on the Attribution page.
- **B11 [L] Author persona.** Invented first-person asides: Ch 2 "I enjoy a good steak... Nobody has ever seen me panic", Ch 10 "I last bit my nails", Ch 28 "I enjoy the fight... glad for the rest of the day", Ch 30 "how you and I got here". Keep "I" for opinions; rewrite these as "a man". Also "I" and "we" drift (Attribution says "we", chapters mix).
- **B12 [L] Overused words** (per 1,000 words): "nothing" 2.3, "trap" 1.5, "a man who" 1.2, "itch" 1.0; also "exactly" 37 uses, "of course" 12, "stop kidding yourself" 3, "pipsqueak" 3. See `checks/word-use.md`.
- **B13 [L] Small style drift.** God's pronoun is lowercase in most chapters (Intro, 3, 6, 8, 13, 26b, 27) but "He" in Ch 17, 19, 20. "Dr Dobson" vs "James Dobson". "If you're an atheist" in Ch 23 and 27 (convention: "not a believer"). Jason Evert is named in Ch 5 and "a Catholic teacher" in Ch 26.
- **B14 [L] Jargon used before it is explained.** "hackbook" (Intro line 240, Ch 33, Attribution), "NoFap" (first in Ch 2 and the Intro, never defined), "edging" (Ch 11, defined in Ch 24), "semen retention" (Ch 4 quote, Ch 13, Ch 19; defined in Ch 21), "fap" in quotes (Ch 3, 8).
- **B15 [L] Unsourced or overstated claims.** Ch 15 "more than a million people have joined forums"; Ch 25 "men who keep a way back fail far more often" (carried from EasyPeasy, no evidence); Ch 28 "Follow these and you cannot fail" (sits beside "failing is no disgrace"); Ch 8 "four marriages" (a commenter's figure, assumptions noted in DRAFT-NOTES).
- **B16 [L] Ch 9 title.** "Advantages of Jerking Off" is the masturbation-only joke at the heart of a book about lust. Keep for the title echo, or broaden to "Advantages of Lust" (James's call).
- **B17 [M] Fit-for-service vs "don't rebuild your life".** Ch 26b says "If you aren't putting your recovery first, you are putting everything else last". Ch 28 and Ch 32 say "change nothing in your life because you've stopped" and "don't rebuild your life around having stopped". Reconcile in 26b (sober first, then get on with life).

## B. By chapter

**Introduction** (index.Rmd)
- 0.1 [M] "Why a hackbook, and why a successor to EasyPeasy?" (line 240) uses undefined jargon and reads like a leftover. Cut or rewrite.
- 0.2 [M] B6: promises Ch 1 explains "not permission to sin".
- 0.3 [L] Long: about 3,500 prose words, with two overlapping fear/good-news sections ("The only thing stopping you is fear", "The good news"). Consider trimming 10-15%.
- 0.4 [L] Quote "I hate it, but I continually feed it" is used here and again in Ch 3 (the repeat is acknowledged in the text).
- 0.5 [L] 3 sentences over 25 words.

**1 The Easy Method**
- 1.1 [M] Two r/TrueChristian quotes unverified (the "human effort" line and "try and try and try"); NOTE in file. James to check or cut.
- 1.2 [M] B6 (explicit answer to "you told me it's a sin").
- 1.3 [L] Repeats the Intro's "carry on as normal" explanation; keep Ch 1 as the fuller home and trim the Intro.
- 1.4 [L] 3 long sentences.

**2 Why Is It Difficult to Stop?**
- 2.1 [L] B11: "I enjoy a good steak" persona line.
- 2.2 [L] "Go back to the week before you started" question: first of seven uses (B4).
- 2.3 [L] 3 long sentences.

**3 The Flesh**
- 3.1 [M] Transition glitch in "Crossing the red line": "you choose the times. They turn out to be four:" is followed by two bullets (two opposite pairs). Reads as a dropped list and breaks the red-line section.
- 3.2 [M] Lewis "He made the pleasures" repeats in Ch 6 (B4).
- 3.3 [L] Five itch analogies in one chapter (alarm, tap, tight shoes, rash, hunger); keep two. Ch 6 adds the rash again.
- 3.4 [L] 2 long sentences. Scope is good here (three doors, "wrong head").

**4 The World's Lies**
- 4.1 [M] "Giving up" section and the eight-item loss list (Energy, Time, Confidence...) pre-empt Ch 6 and Ch 17, which use the same list. Trim to a pointer.
- 4.2 [L] The NoFap thread claim has no URL (DRAFT-NOTES); retraction claim is sourced.
- 4.3 [L] "Semen Retention" quote used before Ch 21 defines it (B14).
- 4.4 [L] 5 long sentences.

**5 The Times We Reach For It**
- 5.1 [M] Psalm 4:8 wording open (B10).
- 5.2 [L] Jason Evert named here, "a Catholic teacher" in Ch 26 (B13).
- 5.3 [L] 6 long sentences. Long chapter (about 3,500 prose words) but the occasion-by-occasion structure holds.

**6 What Am I Giving Up?**
- 6.1 [M] Lewis quote repeated from Ch 3; the "nothing to give up" case is now made in Ch 1, 4, 6, 17 and 20.
- 6.2 [L] Rash-and-cream overlaps Ch 3's rash.
- 6.3 [L] Lust framing is thin (the chase and porn barely appear in "the void").

**7 Getting Your Time Back**
- 7.1 [L] "Chain... forged by the one before" echoes Ch 12 almost word for word.
- 7.2 [L] "No farewell session, only a prayer" repeats Ch 1.
- 7.3 [L] The heading "A conversation" is also used in Ch 8.
- 7.4 [L] Sums check out (30 min a day = 180 hours a year; 7 hours a fortnight).

**8 What It's Doing to You**
- 8.1 [M] Longest chapter (about 4,100 prose words). Two big sections ("The way you see women", "Nobody's lever") sit inside a list of costs, and the death-grip section splits it. Trim the "conversation" and "so far so good" bits, or move "Nobody's lever" to Ch 14.
- 8.2 [L] "A man of forty-three... four marriages" is a different man from the Intro's "43rd year"; the repeat number confuses. Assumptions noted in DRAFT-NOTES.
- 8.3 [L] Forward promise "you won't be straining at the stones, as you'll see" is only loosely paid (Ch 20, 26b).
- 8.4 [L] 9 long sentences (most in the book).

**9 Advantages of Jerking Off**
- 9.1 [L] B16.

**10 The Willpower Method**
- 10.1 [H] B2: lust 1, women 0. Add the willpower story for porn and for the chase.
- 10.2 [L] B11: nails line. Augustine and counters repeated (B4).
- 10.3 [M] 7 long sentences.

**11 Beware of Cutting Down**
- 11.1 [M] Ration argument duplicated in Ch 13 (B4).
- 11.2 [L] Heath Lambert's "radical measures" quote cuts against Ch 25's no-fortress line.
- 11.3 [L] "Edging" used before defined (B14).

**12 Just Once**
- 12.1 [H] B2: lust 1, porn 0, women 0.
- 12.2 [L] "Chain" line repeats Ch 7. Its "three things" list repeats in Ch 20's five.
- 12.3 [M] Strict "just once doesn't exist" vs gentle slip guidance in Ch 28 (B8).

**13 Types of User**
- 13.1 [M] "A week in the life of a ration" duplicates Ch 11; the married-incentive and Dobson lines repeat in Ch 19 (B4).
- 13.2 [M] Length: about 3,700 prose words and 11 types; trim.
- 13.3 [L] "A Christian therapist who has counselled couples for forty years" here and "free of this for nearly forty years" in Ch 15: same man or not? Make clear.
- 13.4 [L] 4 long sentences.

**14 Fantasy and the Thought Life**
- 14.1 [M] Lewis harem line repeated verbatim from Ch 5 (B4).
- 14.2 [L] "What it comes to" recaps Ch 13's porn-free man with no new content.
- 14.3 [L] Good scope ("The woman in the room"); 3 long sentences.

**15 A Secret Habit?**
- 15.1 [H] B2: lust, porn and women are all 0. Secrecy applies to the chase and to porn too.
- 15.2 [L] "More than a million people" unsourced (B15).

**16 Timing**
- 16.1 [M] "NOW" and "carry on as normal" sit together without a clean explanation, and the Intro says "You'll stop right away" (B5).
- 16.2 [L] B2 (women 0). The heading "Three questions" repeats Ch 1's.

**17 Will I Miss It?**
- 17.1 [H] B2: all three counts 0.
- 17.2 [L] Loss list repeated from Ch 4; "wouldn't wish it on his son" again.

**18 Can I Compartmentalise?**
- 18.1 [L] "Only two things hold a man back, opportunity and a body that can only be flogged so far" contradicts Ch 13's four brakes (time, body, privacy, conscience).
- 18.2 [L] The two rooms could include the third face (the double life with women).

**19 Avoid False Incentives**
- 19.1 [M] Duplicates Dobson (13), the marriage incentive (13, 16), and the counter (10) (B4).
- 19.2 [L] "He's not fooled" capital He; "Dr Dobson" (B13).
- 19.3 [L] 4 long sentences.

**20 The Easy Way to Stop**
- 20.1 [H] B2: the two core instructions and "One man's last time" are hand-only. Name lust, porn and the chase in instruction 1 and in the story.
- 20.2 [M] B5: "decide you will never do it again" vs "make no vows".
- 20.3 [L] "Five things" repeats Ch 12's three; "fruit grows on a healthy tree without straining" repeats Ch 3's apple image (also Ch 10).
- 20.4 [M] 5 long sentences.

**21 The First Weeks**
- 21.1 [M] B2: lust 0. The cue list ("bed, shower, empty house, phone at midnight") has no cue for the other faces (a message from her, a scroll).
- 21.2 [L] Wet dreams duplicated in Ch 28 (B4); retention is defined here but used in Ch 4, 13, 19 (B14).
- 21.3 [L] Ch 26 cites figures this chapter does not contain (B9).

**22 Just One Little Look**
- 22.1 [L] Pronoun slip: "His version was a few 'soft' photos. They have no idea what it does to their morale."
- 22.2 [L] Filename says "peek", heading says "Look" (the site slug follows the heading).

**23 Will It Be Harder for Me?**
- 23.1 [M] B2 (hand-centred; "Jerking off won't fix it" is the allowed on-purpose use).
- 23.2 [L] "Atheist" wording (B13). 2 long sentences.

**24 Substitutes**
- 24.1 [M] B9: "tug-of-war from Chapter 11".
- 24.2 [L] "The first four on the list" but the text adds "A woman instead", which is not in the list; add it.
- 24.3 [L] Edging overlaps Ch 11.

**25 Should I Avoid Temptation?**
- 25.1 [M] B5: practical advice (kitchen phone, delete the folder, roommate) has no timing against "carry on as normal until the end", and Ch 28 #6 says "change nothing".
- 25.2 [L] B15: "men who keep a way back fail far more often".

**26 The Moment of Revelation**
- 26.1 [M] B9: cites Ch 21 for figures it doesn't give.
- 26.2 [L] Jason Evert unnamed ("a Catholic teacher"), see Ch 5.

**26b Fit for Service**
- 26.b.1 [M] B1: it carries the whole frame alone.
- 26.b.2 [M] B17: "recovery first... everything else last" vs "change nothing"/"don't rebuild your life".
- 26.b.3 [L] Tone jumps from Ch 26's light "isn't it marvellous" to a heavy military register; one bridging sentence at the end of Ch 26 would soften it. The apostle "James" may confuse readers who know the project (cosmetic).

**27 The Final Step**
- 27.1 [M] B5/B8: the prayer is a vow; the final warning ("not once") vs Ch 28 grace.
- 27.2 [L] "If you're an atheist" (B13).

**28 Feedback**
- 28.1 [M] Duplicates Ch 30's Slipping and tell-her sections, Ch 21's wet dreams, Ch 5's sleep; the checklist "closes this chapter" but isn't last; "cannot fail" overclaim (B8, B9, B15).
- 28.2 [M] Checklist #6 "Change nothing" vs the same chapter's "keep the phone out of the bedroom".
- 28.3 [L] B11: "I enjoy the fight". Length about 2,900 prose words.

**29 Help Those on the Sinking Ship**
- 29.1 [L] B2: lust and porn 0. Overlaps Ch 30's parents section (fences, a father's story).

**30 Advice to Non-users**
- 30.1 [H] B7/B8.
- 30.2 [M] The pebble parody: "I've stolen the idea" undercuts the credit ethic; the idea came to EasyPeasy from Guillaco, who is not on the Attribution page. Say "borrowed, with thanks" and credit.
- 30.3 [M] Duplicates Ch 32's pass-it-on and industry paragraphs (B4).
- 30.4 [L] B11: "you and I got here". 5 long sentences.

**31 The Instructions**
- 31.1 [M] Eleven instructions vs Ch 28's seven vs Ch 20's two: no reconciliation. #7 "Stop now" and #8 "make your vow" omit "carry on until the end" and "no cutting down" as written for the pre-prayer reader. Label this list "After the last page" or merge.

**32 Now**
- 32.1 [M] B1: the soldier is not closed. Add a line in "Back in the fight".
- 32.2 [M] "Send it in" and "translate it" give no address (Attribution has none).
- 32.3 [L] Pass-it-on and industry paragraphs duplicate Ch 30; the Augustine child's-voice detail is embellished.

**33 Appendix**
- 33.1 [M] "Whose voice is that?" says the Little Monster speaks in your voice; Ch 3 defines him as an itch and Ch 30 says "he isn't you". Align with the Big Monster/Little Monster split.
- 33.2 [L] "Hackauthor²... hackbook" (B14). Trimpey essay is retold (DRAFT-NOTES: cut if strict). Crisis numbers (988, RAINN) were confirmed on 2026-11-17.

**FAQ / Why This Book Exists / Attribution**
- W.1 [M] B10: Romans 8:1 "for those" in both FAQ and Why This Book Exists.
- W.2 [L] FAQ typo "and See [What about porn...]". Why This Book Exists line "It helps me sleep. It relaxes me." reads as the author's claim; add quotation marks.
- W.3 [M] Attribution has no contact route and does not name the WEB edition; its HTML NOTES comment lists both.

## C. Mechanical checks

- **Long sentences** (over 25 words, quotations excluded): **94**, in 32 of 38 files. Most: Ch 8 (9), Ch 10 (7), Ch 5 (6), Ch 4, 20, 30 (5 each). None in Ch 9, 22, 24, 31, 33, Why This Book Exists. Full list with line numbers in `checks/long-sentences.md`. A few are splitter false positives (an ellipsis inside a quote).
- **Overused words:** see B12 and `checks/word-use.md`, which also has per-chapter counts of lust, porn, women, masturbation, soldier and "wrong head".
- **Author name:** none in any chapter, the Attribution page, FAQ or Why This Book Exists. Present only in the site and tooling files listed in B3.
- **Spelling:** British throughout; the one "color" is inside a quote.

## D. The two open items (both settled 2026-11-17)

Settled: Psalm 4:8 now reads "for you, Yahweh alone" (WEB, word for word); the two Ch 1 quotes are paraphrases; Ch 9 is titled "Advantages of Lust" (B16).

1. **Psalm 4:8, Ch 5:** "for you alone, Yahweh" (ebible.org, now) vs "for you, Yahweh alone" (older WEB). Pick the edition; name it on the Attribution page. (B10)
2. **Ch 1, two r/TrueChristian quotes** (the "human effort" line and "try and try and try"): unverified; Reddit can't be reached from here. James to check while logged in, or cut. (1.1)

## E. Counts

**119 issues: 10 H, 45 M, 64 L** (17 book-wide, the rest by chapter).

Most work needed, in order: Ch 30, 20, 8, 13, 28, 10, 31, 32, 26b, 21, 12, 15, 17. Cleanest: Ch 1, 2, 6, 7, 9, 22, 24, 29.

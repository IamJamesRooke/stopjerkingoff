# Quote and verse verification

Checked 2026-11-14 against `main` at ee8dfde, which is the revised book with Revision 3 complete. No chapter was edited. Each fix below gives the file, the exact current text, and the correct text, so the author can apply them all in one pass.

## Summary

| What | Checked | Result |
|---|---|---|
| Bible verses (WEB) | 66 quoted verses and fragments, plus every reference | **1 wording error** (Psalm 4:8). Every reference points to the right verse. |
| Quotes with a SOURCES entry | 298 | 285 confirmed word for word. A few small sites rely on the earlier check run the same day. 1 needs a wording fix (Ch 21) and 1 is a caption judgement call (Ch 26). 9 match the research captures but couldn't be reopened today, and 2 can't be reached (Reddit). Separately, 1 link is wrong and 2 SOURCES lines lack a link. See below. |
| Piper paraphrases (open item 1) | 9 | **All 9 confirmed on desiringgod.org.** The quote marks can go back. |
| "Verify wording" items (open item 3) | NPR/Grubbs, Ashley Willis | Both confirmed word for word. |
| YouTube auto-caption quotes (open item 2) | 108 | All checked against each video's own transcript panel or comments. 1 wording fix and 1 judgement call. |

**How it was checked.** Verses were compared against the full WEB text (TehShrike/world-english-bible JSON, the edition with "Yahweh"), ignoring case and punctuation. Quotes were matched from the body to their SOURCES lines. Each source page was then opened in Chrome and searched for the exact words, ignoring punctuation and case. Ellipses were treated as gaps. Most YouTube quotes were checked against the video's transcript panel; FitXFearless quotes were checked against the saved transcripts in research/transcripts. Invented dialogue and the author's own self-talk in quote marks (about 360 lines) aren't sourced quotes, so they weren't checked.

## Fixes to apply

### 1. Psalm 4:8 wording (Ch 5)
- **File:** `05-the-times-we-reach-for-it.Rmd` (body, the paragraph beginning "When you stop, you may have two or three nights")
- **Current:** "In peace I will both lay myself down and sleep, for you alone, Yahweh, make me live in safety."
- **WEB:** "In peace I will both lay myself down and sleep, for you, Yahweh alone, make me live in safety."

### 2. QuitByHealing caption wording (Ch 21)
- **File:** `21-the-first-weeks.Rmd`, body (line beginning "A recovery coach tells a story") and the SOURCES line for Dgvg8Je9Jdk
- **Current:** "and then I got home I didn't do anything because the feeling had already passed"
- **Captions say:** "but then once I got home I didn't do anything because of the feeling had already passed"
- **Suggested:** "once I got home I didn't do anything because ... the feeling had already passed". The ellipsis drops the caption's stray "of".

### 3. Wrong video link for the partner's comment (Ch 30)
- **File:** `30-advice-to-non-users.Rmd`, SOURCES line for "I was not told about it until late in the relationship."
- **Current:** "https://www.youtube.com/watch?v=SexciPjCC0s or https://www.youtube.com/watch?v=6BzPBrlE6RA (research/round2/death-grip.md gives both; confirm which)"
- **Correct:** https://www.youtube.com/watch?v=6BzPBrlE6RA (Noah B.E. Church, "How to Heal Delayed Ejaculation"). The comment is under that video, not Dr Malik's.

### 4. Wrong Piper URL (Ch 5, 25 and any other "Strategies" link)
- **Files:** `05-the-times-we-reach-for-it.Rmd`, `25-should-i-avoid-temptation.Rmd` (SOURCES)
- **Current:** `https://www.desiringgod.org/articles/strategies-for-fighting-sexual-sin`. This link returns 404.
- **Correct:** `https://www.desiringgod.org/messages/strategies-for-fighting-sexual-sin`
- Ch 30 cites the gospeltranslations.org copy. Switch it to the desiringgod.org link above too.

### 5. Add missing source links
- **Ch 14** `14-fantasy-and-the-thought-life.Rmd`, SOURCES for "The easiest thought for me to say, 'No' to, is the first one. ..." currently reads "talkingsober.com thread 197816". Add `https://talkingsober.com/t/struggling-with-fantasies/197816`. The wording is confirmed there.
- **Ch 4** `04-the-worlds-lies.Rmd`, SOURCES for "Semen Retention does not grant you godhood." names the NoFap forum thread "Semen Retention is bullshit, emissions are inevitable" (14 Mar 2019) but gives no URL. The wording matches the research capture. The thread couldn't be found again without a forum login, so add its link before print or keep it as it is.

## Optional: restore the Piper quotes (open item 1)

All nine Piper lines are confirmed word for word on Desiring God. The paraphrases can become quotes again. The current text is on the left of each arrow and Piper's exact words are on the right.

From ["Missions and Masturbation"](https://www.desiringgod.org/articles/missions-and-masturbation):
- `index.Rmd`: "take it for granted that most single men do it" → Piper calls it "a regular practice of most single men."
- `04-the-worlds-lies.Rmd`: "grant that virtually every man has tried it, and almost as many women" → "Virtually every man and almost as many women have tried it."
- `08-what-its-doing-to-you.Rmd`: "he felt unworthy and unable to obey the call of God. His conclusion was blunt: masturbation becomes the enemy of missions." → "feels unworthy and unable to obey the call of God." / "Masturbation becomes the enemy of missions."
- `29-help-those-on-the-sinking-ship.Rmd`: "he is not alone in this" → "You are not alone in the battle."

From ["Strategies for Fighting Sexual Sin"](https://www.desiringgod.org/messages/strategies-for-fighting-sexual-sin):
- `05-the-times-we-reach-for-it.Rmd`: "never assume that you deserve relief through sin" → "Never assume that you are above suffering or that you deserve relief through sin."
- `25-should-i-avoid-temptation.Rmd`: "be vigilant over your eyes, and avoid unnecessary stimulation" → "Be vigilant over your eyes. Avoid unnecessary stimulation."
- `30-advice-to-non-users.Rmd`: "get into a group where they warn one another, daily, against the deceitfulness of sin" → "Get in a group where you exhort one another every day against the deceitfulness of sin."

Update the matching SOURCES notes ("could not be checked") to say they were checked on 2026-11-14.

## Couldn't be verified

- **Ch 1, two r/TrueChristian lines** ("anything that required 'human effort' ultimately failed me ..." and "The more you try and try and try to stop thinking about porn ..."), from https://www.reddit.com/r/TrueChristian/comments/larhm7/. Reddit is blocked from the research machine and from the browser extension, and no mirror copy was found. Either James checks them while logged in to Reddit, or they come out. The other eight Reddit quotes in the book were confirmed on the Your Brain On Porn pages that reproduce them.
- **Five YouTube comments under Ezekiel's video** (mppw_mrhlIY): "You need to stop 'keeping scores'...", "GOD TOLD ME I COULDN'T KILL SOMETHING...", "When I was married, I bought that into my marriage...", "I would repent, be fine for a couple/few weeks, then BAM!", "The shame of it ... made me not want to pray or talk to God." They match the research capture, which was copied from the page. They didn't load again among the top comments today, which is normal because YouTube reorders comments. Low risk.
- **Dobson (dobsonlibrary.com)** wouldn't load today (error page). Both lines were confirmed word for word in the earlier check on the same day.
- **ro.co** sat behind a bot check today. The same line was confirmed in the earlier check.

## Judgement calls (no change needed unless James wants one)

- **Ch 26, Captain Sinbad:** the captions read "finally singing in color". The book's "seeing" is almost certainly what he said, and the SOURCES note already says so. To be strictly faithful, write "[seeing]".
- **Ch 15, Dr Doug Weiss:** the captions repeat "when I was in, when I was in school". The book drops the stutter. That's normal cleanup.
- **Ch 10:** "tomorrow, and tomorrow?" The Georgetown Pusey text has "to-morrow, and tomorrow?" The SOURCES note already says the spelling follows Gutenberg. Cosmetic.
- **Ch 30, Ashley Willis:** both lines are confirmed. The article doesn't say her husband is a pastor, so "one pastor's wife" still rests on general knowledge (Dave Willis). Consider "one wife" unless confirmed.
- **Ch 8, "her":** the Covenant Eyes comment "then feeling like a great failure to God, her, and myself" is about his wife. The same comment mentions "our 20th ann". Confirmed.
- **Index, "Before I ever watched porn ...":** this is Ezekiel speaking in the video, not a commenter. The SOURCES note is correct.

## Earlier quote-check items, now resolved in the book

Every fix from research/round2/quote-check.md is now in the book: "more than a million people" (Ch 15), the Rogers and Tarwater lines removed (Ch 13, 18, Appendix), the Reddit mirror quotes replaced, the "gave it away" SOURCES note (Ch 32), and Gaariv's talkingsober link (Index).

## Still open from DRAFT-NOTES Revision 3 (not quote work)

Items 4 (helpline numbers), 6 (overlap re-run), 7 (lengths), 8 (first-person anecdotes) and 9 (attribution contact) weren't part of this check.

# Method Check: Is the Book Still the Easy Way?

Whole-book audit, 2026-11-19, against main at commit 645895a. Every chapter from the Introduction to Chapter 33 was read, plus the FAQ and "Why This Book Exists". No chapter text was changed. The Author thread applies the fixes.

Line numbers point at the `.Rmd` file on main as of that commit.

## Verdict

**The book has not drifted far. The method still carries it.** The logical chain is intact and in the right order: fear keeps you in, not desire. The Little Monster is tiny. The Big Monster is the lies. Each illusion of benefit is taken apart in turn. There is nothing to give up. Willpower, cutting down, "just once", substitutes and counting days all fail. Then you decide and rejoice, you don't wait for the moment, and you never take the one. Chapters 1 to 3, 5 to 7, 11 to 13 and 21 to 25 are as faithful to EasyPeasy as anything in the book. In places they are clearer.

The drift is local, and it falls into four kinds:

1. **The final step has lost some of its joy.** The vow primes struggle ("easy or hard"). The Christian prayer leaves out the one idea the whole method rests on ("it gave me nothing"). A danger checklist comes straight after "YES! I'M FREE!".
2. **Guilt is piled up just before the decision.** "Fit for Service" retells David and Uriah a second time in full and ends on "Somebody else always pays". It is the last thing a man reads before the vow.
3. **A few lines quietly bring back willpower, avoidance or shame.** There is an instruction to act mid-book ("cancel the subscription and block the page tonight"), a quote that says stop "for a time", and the phone-out-of-the-bedroom tip repeated until it reads like a rule. The website still says "carry on as normal".
4. **Long additions bury the chain in three chapters:** Chapter 4 (the porn industry), Chapter 14 (the portraits, Samson and Ahab) and, more mildly, Chapter 15.

What does **not** need fixing: the Christian frame, "fit for service", the two Monsters, the safety box, the softer final step with no last session, If You Slip, the sections for wives and parents, and the honesty about medicine. None of these works against the method. Several of them strengthen it. Grace removing guilt is the strongest anti-shame tool the book has.

---

## Ranked fixes

Ranked by how much each one helps the method work for the reader. H = high, M = medium, L = low.

### H1. The vow primes a struggle: "Whether I find it easy or hard"

**Where:** `28-the-final-step.Rmd:50` (prayer) and `:64` (the version for men who don't pray).

**Problem:** EasyPeasy's two checks just before the vow are "Are you certain?" and "Are you excited?", and this chapter asks them at lines 13 and 14. Then, in the vow itself, the reader says out loud that it might be hard. That is the Willpower Method's own expectation, put in his mouth at the most important moment of the book. It also goes against the Introduction's promise of "free of misery, free of willpower".

**Fix:** In both versions, replace
> Whether I find it easy or hard, my answer is No.

with
> My answer is No, and I give it gladly.

Read aloud, this lands on "gladly", which is the note the method wants.

### H2. The Christian prayer leaves out the heart of the method

**Where:** `28-the-final-step.Rmd:44-56`.

**Problem:** The secular version carries the method: "I'll do it by remembering what I now know: it gave me nothing." The prayer has confession, forgiveness, a No and a request for strength, but nothing about seeing through the lie. So a believer could pray it as one more willpower vow with God as witness. That is exactly the vow Chapter 1 ruled out, and the "But I've promised this before" section (lines 20-26) says this decision differs because "there's nothing left that you want from it". The prayer should say that.

**Fix:** After "Make me clean." (line 48), add one short paragraph:
> It never gave me anything. I am not giving anything up. I am being set free.

### H3. A danger checklist straight after "YES! I'M FREE!"

**Where:** `28-the-final-step.Rmd:88-100` ("The first three days").

**Problem:** The reader shouts "YES! I'M FREE!" and "Do it now", and the very next thing he reads is a to-do list: clear the phone, delete the app, expect the bell, tell someone before the deadline, "If you fall, read If You Slip the same hour." Each line is sensible. Together, at this point, they tell him he is now in danger and must manage it. That is the mood the method exists to avoid. The chapter then goes back to joy ("Let it ring", "You are already free"), so the checklist breaks the flow as well.

**Fix (Author's choice of wording):**
- Cut the heading and the list as a block.
- Fold the two method lines into "Let it ring" (line 102 on). "Know your hour. A bell you saw coming is only a bell." "If you lie awake, lie there and be glad. You know what is dying."
- Drop the "Tonight, clear the way" bullet. Chapter 26 already covers it with the right framing ("sense, not fear").
- Drop "If you fall..." here. The final warning at line 134 already points to If You Slip, which is enough.
- Keep "Tell one person you trust", but move it into "You are already free" without the 72-hour deadline. Something like: "In the first week or so, tell one person you trust, as a free man giving news. Chapter 29 says how." A deadline turns good news into a test.

### H4. "Fit for Service" puts a guilt peak just before the vow

**Where:** `27b-fit-for-service.Rmd:21-33` ("The king on the roof").

**Problem:** EasyPeasy wants the reader elated, not burdened, as he reaches the final step. This chapter is the last thing he reads before the vow, and its middle section retells David and Uriah in full. That is the second full telling, after Chapter 9 (Chapter 5 and Chapter 23 mention it too). It ends: "A woman was used, a good man was buried, and a child died ... Somebody else always pays." The "Who gains?" section and the Isaiah ending are strong and on-method. "You were worth taking out of the fight" and "being fit is not the price of being loved" lift him. The retelling pulls him back down.

**Fix:** Keep the chapter and the frame. Cut "The king on the roof" down to the one point it adds that Chapter 9 doesn't make, the contrast between the two men. For example:
> You know King David's story: the roof, the bath, his soldier Uriah sent back to die. Notice one thing about it. Uriah, even drunk, slept at the palace door like a soldier on duty. David, sober, was the weak point in his own army. Lust had taken the commander off the field without a fight.

Delete "Somebody else always pays." and its paragraph (lines 31-33). Chapter 9 already carries that weight, much earlier, where the book can afford it.

### H5. The website still says "carry on as normal"

**Where:** `why-this-book.Rmd:29`.

**Problem:** The pastor review removed "carry on as normal" from the book because it reads as an instruction to keep sinning. James approved that fix. The website's own article still says "You carry on as normal until the last page." For many readers this is the first page they see.

**Fix:** Replace the bullet with the book's own wording, as in the FAQ:
> **No willpower campaign while you read.** Make no vows, start no streaks, and don't cut down. Just keep reading to the last page. Starting a willpower campaign halfway through a book that's about to make willpower unnecessary only gets in the way.

### H6. An order to act in the middle of the book: "cancel the subscription and block the page tonight"

**Where:** `14-types-of-user.Rmd:44` (end of "The man who pays").

**Problem:** It breaks two rules at once. It is an action halfway through the book, before the reader is told to stop (Introduction and Chapter 1: no willpower campaign). And "block the page" is the fortress that Chapter 26 warns against.

**Fix:** Replace
> If this is you, add up what you have paid this year and look at the number. Then cancel the subscription and block the page tonight.

with
> If this is you, add up what you have paid this year and look at the number. Then ask what it bought you.

On the final step, the cancelling happens naturally: the decision covers "using a woman", and Chapter 26 already says "Unfollow the accounts". If the Author wants it said outright, add "Cancel the subscriptions" to that Chapter 26 sentence, where it is framed as sense.

### M1. Chapter 4's porn-industry section puts the guilt on the reader

**Where:** `04-the-worlds-lies.Rmd:27-37`, especially line 31 ("A man who watches takes part in whatever was done to make it.") and line 35 ("That is prostitution ... Porn is the crack.").

**Problem:** The section has a sound method job: it demolishes the lie "nobody gets hurt". But it reaches the reader in Chapter 4, while he is still in the trap and has been told to keep reading without a campaign. Lines like "takes part in whatever was done" and "You have [paid for sex]" make him a perpetrator. Chapter 1 says guilt "loads the gun", and this section loads it. It is also about 600 words, inside the chapter that carries the Big Monster. That makes it the longest single stretch between "The flesh supplies the itch" and "Giving up".

**Fix:**
- Keep the facts (the 2020 report, the trafficking case, the fake videos). They are true, and they take an illusion away.
- Recast the reader as the man who was deceived, not the man who is guilty. For line 31, replace the last two sentences with: "Nobody told him. He was sold it as harmless entertainment, and so were you. It never was."
- In line 35, keep "Your visit is the money" and the crack line if the Author likes them; they read aloud well. Cut "That is prostitution, with a camera between her and you", which says the same thing more harshly.
- End the section with one line that ties it back to the method, so it doesn't stand as a sermon: "This isn't here to add to your guilt. It's here to take away the last excuse. You don't need it, and it was never harmless."

### M2. Chapter 14's job is buried

**Where:** `14-types-of-user.Rmd`, the longest chapter in the book (about 4,500 words). Samson runs from line 72 to 96, and Ahab from 98 to 106.

**Problem:** EasyPeasy's chapter on types has one job: no type is better off, and it's one trap at different depths. Lines 7-47 and the closing paragraph (150-152) do that job well. In between come the collector, Samson (about 900 words, told in full with all three ropes), Ahab, the married man, imagination, and the church guy. Samson and Ahab are morality tales about women leading a man, not mechanism. By the end, the reader has lost the thread back to "you don't need to envy any of them". James moved Samson and Ahab here this morning (commit 83ad965), so they stay. They should just be shorter.

**Fix:**
- Samson: keep the opening, "He isn't fooled. He just can't leave" (line 78), and the hope ("the hair of his head began to grow again", line 86, and "he still hears that prayer", line 96). Tell the three ropes in one sentence instead of two paragraphs. Shorten the temple scene to three or four sentences. Target: about half the length.
- Ahab: two or three sentences, keeping "he 'sold himself'" and "Being sorry is not the same as turning around."
- Collector, line 67: cut "Here is a question for any man, believer or not. If you had lived as though the Christian rules were true...". It is an apologetic aside in a chapter about the trap.
- Keep "The man who pays" and "The man with a machine" as they are, apart from H6. They are portraits of the trap, which is what this chapter is for.

### M3. A quote that says stop "for a time"

**Where:** `12-beware-of-cutting-down.Rmd:64`.

**Problem:** "Most people cannot conquer lust until they stop masturbating for a time." The chapter then says "He doesn't say cut down. He says stop." But the quote itself says stop *temporarily*. In the chapter against half-measures, that is the one phrase a man looking for a loophole will catch.

**Fix:** Cut the pastor's quote and keep the chapter's own words: "A pastor writing about this habit reached the same place from the other direction. He doesn't say cut down. He says stop. A limit is indulgence with a schedule." The commenter's line that follows ("he couldn't kill something he continued to feed") carries the point better anyway.

### M4. The phone out of the bedroom has become a rule

**Where:** `22-the-first-weeks.Rmd:78`, `26-should-i-avoid-temptation.Rmd:56`, `28-the-final-step.Rmd:92`, `32-the-instructions.Rmd:9`, `31-advice-to-non-users.Rmd:65` (parents).

**Problem:** Chapter 26 frames it exactly right: "because bed is a stupid place for a phone at midnight ... not because you're in danger." Repeated across five chapters, though, including the final step and the one-page rules, it becomes the kind of safeguard EasyPeasy warns against: a fence that tells you the thing is still dangerous.

**Fix:** Keep it in Chapter 26 (and in the parents' section, where it's about children). Elsewhere:
- Ch 22:78, change to: "I'm tired. Tired men believe lies more easily. I'll go to bed."
- Ch 28:92, removed as part of H3.
- Ch 32:9, change to: "Refuse every stopgap and every substitute."

### M5. Two lines that shame instead of freeing

- `13-just-once.Rmd:29`: "A weak moment isn't a crime. Choosing a lifetime of that, when you could be free, comes close." The second sentence calls the reader nearly a criminal for staying in the trap. Fix: "A weak moment isn't a crime. But why choose a lifetime of that, when you could be free?"
- `22-the-first-weeks.Rmd:44`: "Usually it's as simple as standing up and leaving the room." Read in the first weeks, this teaches escape, the reflex Chapter 26 calls the fortress. Fix: "Usually the way out is simply to let the moment pass." That echoes "Let it ring" and the do-nothing instruction from the same chapter (line 26).

### L1. Chapter 15 runs long, but stays on-method

**Where:** `15-fantasy-and-the-thought-life.Rmd:85-107` (dating apps, "the one girl", pictures).

All of it is relevant, and the chapter ends well ("You don't have to fight it yet. For now, just watch."). If the Author wants to trim one thing, the pictures paragraph (line 105) is the most rule-based ("A free man doesn't ask for it. If she offers, he says no"). It could become one sentence: "Asking for a picture is making your own porn, with a woman you know." No change is required.

### L2. Chapter 29's sex section leans toward a sermon

**Where:** `29-feedback.Rmd:121` ("Look at what we've all been sold ...").

It is a culture-war paragraph inside a Q&A chapter, and it comes after the reader has decided. It is harmless to the method, since he has already stopped, but it is the most preachy paragraph in the back half. Optional: cut it to its first two sentences and its last.

### L3. The 72-hour deadline and the after-slip disclosure

- The "Tell one person before the three days are up" deadline is handled in H3.
- `29b-if-you-slip.Rmd:17`: "If you're married, tell your wife as well, and tell the man you told." That is a firm rule after every slip. It is pastorally sound, and James approved the pastor's line on honesty in marriage. Flagged only because fear of telling her can itself become the reason a man hides a slip, which is the secrecy Chapter 16 warns about. No change suggested unless the Author sees a gentler wording, such as "don't start a new secret".

---

## Checked and on-method (no change)

| Principle | Where it is carried | Status |
|---|---|---|
| Fear, not desire, keeps you in | Intro "The only thing stopping you is fear"; Ch 5 "What an urge really is"; Ch 8 "Both sides of the rope are fear"; Ch 26 | Strong |
| No illusion of benefit | Ch 1 "Three questions" ("I'm saying there are no benefits"); Ch 3; Ch 5 occasion by occasion; Ch 6 itch-and-cream; Ch 10 blank page | Strong |
| Little Monster and Big Monster | Introduced Ch 3 and Ch 4; used consistently through Ch 33 | Consistent |
| No "giving up" or sacrifice | Ch 4 "Giving up"; Ch 6; Ch 20; Ch 25; Ch 28 "Don't build your life around having stopped" | Strong |
| No cutting down | Ch 12; Ch 25 "same thing in a smaller glass"; FAQ | Strong (fix M3) |
| No willpower | Intro; Ch 1; Ch 11 (Romans 7 is an excellent fit); Ch 21 | Strong |
| Don't avoid temptation as a crutch | Ch 26 fortress and dare; Joseph | Good (fixes H3, H6, M4 trim the leaks) |
| "Just once" doesn't exist | Ch 13; Ch 23; Ch 27 three-week trap; Ch 28 final warning | Strong |
| No counting days | Ch 11 "The counter"; Ch 20 badge; Ch 29b pebble forum | Strong |
| The moment you know, and don't wait for it | Ch 27 (the "dawn" caveat is a good addition); Ch 29 Q&A | Strong |
| The final step as a joyful decision | Ch 28 checks for certainty and excitement; "YES! I'M FREE!"; "prisoner's sentences" | Good (fixes H1, H2, H3) |
| Fear tactics | Intro "Warning"; Ch 8 promises no shock treatment; death grip told with honest caveats | Kept honest. Ch 30's sextortion facts are aimed at parents and are appropriate. |
| Grace against shame | Intro; Ch 21 ("God is good, not the fact that you are bad"); Ch 29b "Wanting it to hurt" | This is the book's best addition to the method |

## Note for the Author

Apply in this order: H1 to H6 first (they are short and change the most), then M1 to M5. Keep L1 to L3 for your judgment. Read each changed passage aloud. The replacement lines above were written to be spoken, but check them in context. After the changes, run `tools/editorial_checks.py`, and add a "Revision" line to DRAFT-NOTES.md as usual. For chapters James has already approved (Intro and Ch 1 to 3), none of these fixes touch them except H5, which is the website article, not the book.

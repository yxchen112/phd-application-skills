# De-AI pass for application documents (mandatory, automatic)

Run this on every draft, revision and translation back into English of an SOP, personal history statement, research proposal, cover email or short answer. The user should never have to ask for it. Goal: prose that reads like a careful applicant wrote it. This is not detector evasion: detectors judge statistical predictability, and trimming words rarely changes their verdict.

Distilled and adapted for academic application writing from: `humanizer` (blader, MIT; based on Wikipedia's "Signs of AI writing"), `stop-slop` (Hardik Pandya, MIT), `no-ai-slop` (Peter Yang, MIT), and corrections the applicant made by hand on real drafts. Rules are paraphrased, not copied.

## 0. Principles
- **Minimum effective edit.** Fix the tells, errors and repetition; leave clear sentences in the applicant's own words alone, even if they are plain. A rough sentence with a real voice beats a polished generic one.
- **Never invent** a fact, number, date, motive or source to make a sentence "more specific". If a sentence needs a detail you do not have, ask or cut it.
- **Portability test.** If a sentence could move unchanged into another applicant's statement, it is filler: cut it or replace it with a fact only this applicant has (a system, a number, a decision, a place).
- **Show, don't label.** Facts and decisions carry the emphasis. Delete commentary that tells the reader a point is important, surprising, hard or meaningful.

## 1. Words and phrases
- **Banned words**: delve, foster, leverage, utilize, facilitate, empower, streamline, robust (unless a defined technical sense), cutting-edge, state-of-the-art, paradigm shift, game changer, tapestry, realm, beacon, landscape, multifaceted, meticulous, intricate, paramount, pivotal, transformative, elevate, embark, harness, navigate (challenges), unlock, journey, passion/passionate, dream, fascinated, profound, invaluable, holistic, synergy, underscore, showcase, testament.
- **Empty adverbs** (cut unless they carry a real contrast or uncertainty): really, just, truly, deeply, genuinely, simply, actually, fundamentally, inherently, inevitably, importantly, crucially, interestingly, successfully, significantly (unless statistical).
- **Filler phrases**: it is worth noting, it is important to note, at its core, when it comes to, in today's world, in terms of, with regard to, in order to (→ to), plays a vital/crucial role, serves as (→ is), the reality is, moving forward.
- **Self-praise adjectives**: efficient, productive, innovative, rigorous, dedicated, hard-working, independent, resourceful (the last two only after the episode that shows them, at most once, and only when a prompt asks for them).

## 2. Sentence structures
1. **Binary contrasts**: "not X but Y", "not just X but also Y", "X isn't the problem; Y is", "rather than only X". State Y directly. Keep a contrast only when the contrast itself is the finding.
2. **Negative listing**: "not a X, not a Y, but a Z". Say Z.
3. **Colon reveals and setups**: "The key insight: …", "What I learned was simple: …", "Here is why: …". Write the plain sentence. Colons are for lists and labels.
4. **Rhetorical questions answered at once.** A single explicit research question in the plan paragraph is fine (SKILL.md move 2); a self-answered question for drama is not.
5. **Trailing -ing analysis**: "…, highlighting / reflecting / demonstrating / underscoring my commitment to …". Cut, or replace with the concrete consequence ("so the model could run on noisy inputs").
6. **Importance puffery**: "marked a turning point", "a pivotal moment", "shaped who I am", "solidified my resolve". State what happened and what you did next.
7. **Moral or quotable kickers**: a paragraph-final line that turns the point into an aphorism ("…because a model is only as good as its physics"). Delete it; end on the last concrete sentence. If the paragraph needs closure, add a plain consequence or next step.
8. **Summary-recap endings**: "In conclusion", "Ultimately", "Overall", or a close that re-lists the essay. End on the long-term goal plus one concrete reason (SKILL.md rule 13).
9. **False agency**: "my curiosity led me to", "the project taught me", "the data told us", "the question emerged". Name the actor: "I", the group, the advisor.
10. **"From X to Y" range sweeps** and **rule-of-three lists**: prefer two items; keep three only if each item carries weight; never two triads in a row.
11. **Wh- and "This" openers**: "What surprised me was …", "This experience showed …". Lead with the subject and the specific thing.
12. **Synonym cycling**: if "stress field" is the right word, repeat it; don't rotate stress field / tensor field / polymer state for style.
13. **Self-narrating method or virtue**: sentences that describe how the applicant writes, teaches or thinks ("I avoid jargon and start from problems they already know", "I always look for the physics behind the data"). Replace with one episode that shows it, or cut. The applicant flagged exactly this kind of line as AI-sounding.
14. **Meta-commentary**: "In this statement I will…", "As mentioned above", "Let me explain". Delete.
15. **Narrator from a distance**: "Many students face…", "People often assume…". Write the applicant's own case.

## 3. Rhythm and form
- Sentences ≤ 30 words where possible; split anything that needs a reread. No lists nested inside lists.
- Vary length: three sentences of the same shape in a row → break one. Not every paragraph ends with a short punchy line.
- Vary paragraph openings; no run of "I…" / "In…" starts; no "Also," / "Additionally," / "Furthermore," to bolt on a project.
- **Em dashes**: none in short texts; at most one or two in a two-page statement. En dashes in proper names (Rayleigh–Bénard) and ranges are fine.
- No bold, headers or bullets inside an SOP/PHS body unless the program asks for them.
- Every "it/this/such/these" has an obvious referent in the same or previous sentence.
- A signature word (faithful, trust, long-run, robust, physical) at most twice per document.
- Concrete nouns (stress field, rollout, nozzle, DNS run) over abstract stacks (admissibility, faithfulness, variability).
- **Academic adaptations** of general de-AI rules: technical terms the reader needs stay (do not dumb down a fluid-mechanics committee's vocabulary); passive voice is acceptable when the actor is obvious or irrelevant ("the solver uses FENE-P"), but the applicant's own decisions are always in active voice with "I"; hedges stay when they state real uncertainty ("which suggests").

## 4. Final read (do it every time)
1. Read the whole text aloud in your head. Rewrite anything the applicant would not say to a professor across a table.
2. Ask: "What makes this obviously AI-generated?" List the remaining tells briefly, fix them, then ask once more.
3. Delete any sentence whose removal loses no fact.
4. Each paragraph has at least one plain detail only this applicant could write.
5. Check facts did not drift during editing (numbers, dates, venues, author order, status), and the Chinese side-by-side copy still matches the English.

## 5. Quick score (report with every delivered draft)
Rate 1–10: directness (statements, not announcements), rhythm (varied, not metronomic), trust (no hand-holding or labels), authenticity (sounds like this applicant), density (nothing cuttable). Below 40/50: revise before delivering. Report the score and list the tells fixed, in one or two lines; do not pad the report.

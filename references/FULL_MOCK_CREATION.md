# TOEFL Full Mock Creation Reference

This file is for agents creating new full mock tests in the post-January 21, 2026 TOEFL iBT format. Do not use this file to claim an official ETS subtask distribution. Follow the repo contract and validation rules.

## Section Order

1. Reading
2. Listening
3. Writing
4. Speaking

## Section Totals

- Reading: 50 items
- Listening: 47 items
- Writing: 12 items
- Speaking: 11 items

## Durations

- Reading: 30 minutes
- Listening: 29 minutes
- Writing: 23 minutes
- Speaking: 8 minutes

## Important Note

These totals are the target structure used by this mock system. Subtask distributions must not be labeled as official, fixed ETS distributions. Agents should follow the technical requirements and current repo contract while creating a balanced distribution.

## Reading

Reading must include these task types:

- Complete the Words
- Read in Daily Life
- Read an Academic Passage

Rules:

- Total Reading item count must be exactly 50.
- Before generating Complete the Words, read `references/COMPLETE_WORDS_STYLE.md`.
- Before generating Read in Daily Life, read `references/READ_IN_DAILY_LIFE_STYLE.md`.
- If an Academic Passage reference exists, read it before generating Academic Passage items.
- Multiple questions from the same passage are normal.
- Do not confuse repeated passage display with item count.
- Item count must be calculated by question or blank logic.
- Difficulty distribution should be balanced.
- The section should not be entirely too easy or too hard.

Reading quality balance should include a mix of:

- main idea
- detail
- inference
- vocabulary/context
- grammar/morphology

## Listening

Listening must include these task types:

- Listen and Choose a Response
- Listen to a Conversation
- Listen to an Announcement
- Listen to an Academic Talk

Rules:

- Total Listening item count must be exactly 47.
- Script text must not be shown to the user.
- Audio playback must happen through the mock UI.
- Conversations should use different speaker roles.
- Avoid using the same voice repeatedly for every role when possible.
- Preserve student, staff, professor, lecturer, and announcer distinctions.
- Multiple questions may come from the same script.
- Questions may include a mix of main idea, detail, inference, purpose, attitude, and function.
- Distractors must be plausible.
- Wrong options must not be silly or unrelated.

Audio rules:

- Do not break the existing voice-selection system.
- If Mac system voices or `SpeechSynthesis` are used, preserve the current quality voice mapping.
- Do not allow more than one audio item to play at the same time.
- Preserve play-once behavior when it exists.

## Writing

Writing must total exactly 12 items.

Task types:

- Build a Sentence
- Write an Email
- Write for an Academic Discussion

Rules:

- Build a Sentence items may make up most of the Writing total.
- Include exactly 1 Write an Email item.
- Include exactly 1 Academic Discussion item.
- Total Writing item count must still be exactly 12.
- Build a Sentence items must use phrase/block ordering.
- Correct order must be unique and clear.
- Free-response writing tasks must not be auto-scored as simply right or wrong.
- User responses must be exported.

## Speaking

Speaking must total exactly 11 items.

Task types:

- Listen and Repeat
- Take an Interview

Rules:

- Listen and Repeat prompts should be short, natural, and speech-like.
- Take an Interview questions should ask for short spoken responses.
- Do not break the MediaRecorder recording system.
- All speaking recordings must be included in the export package.
- Total Speaking item count must be exactly 11.

## Question Reuse Policy

When creating a new full mock:

- Do not use the same question ID twice inside the same mock.
- Avoid reusing questions from previous mocks when possible.
- Especially avoid recently used questions.
- If there are not enough unused questions for a new mock, generate new questions first.
- Never change existing IDs.
- Use unique IDs for new questions.
- Follow `AGENT_DATA_CONTRACT.md` for ID ranges and naming conventions.

## Difficulty Balance

A full mock must not contain only easy questions or only hard questions. It should contain mixed difficulty appropriate for TOEFL target levels.

Recommended difficulty mix:

- easy
- medium
- medium-hard

If the agent stores difficulty metadata, it must follow the existing schema.

## Passage / Script Reuse

The same passage or listening script may support multiple question IDs.

When doing this:

- Do not confuse passage/script ID with question item count.
- Calculate total item count by question count.
- Questions from the same passage should not repeat the same skill.

Example:

The same internship email may support:

- a main purpose question
- an inference question

## Mock Definition

When a new mock is created, add a new unique test ID in `data/tests.json`.

Example naming:

- `mock_002`
- `mock_003`

Do not reuse existing mock IDs.

The mock definition must follow the existing schema and include:

- test ID
- test name
- section question references
- section durations
- metadata if the schema requires it

## Full Mock UI

Do not change UI code unnecessarily when creating a new mock.

If new content can be added through `data/questions.json` and `data/tests.json` only:

- Do not change `mock/index.html`.

Only change UI code when a new schema field or real function requires it.

Section order:

```text
Reading -> Listening -> Writing -> Speaking
```

Timer rules:

- Timer should be section-based.
- When time expires, the section should automatically complete.
- Existing answers should not be lost.

## Export for ChatGPT

Preserve the existing "Export for ChatGPT" function.

The export ZIP must include at least:

- `result.json`
- `writing/email.txt`
- `writing/academic_discussion.txt`
- `speaking/*.webm`

When possible, `result.json` should include:

- test_id
- test_name
- timestamp
- section item counts
- section durations
- Reading raw score
- Listening raw score
- Build a Sentence raw score
- used question IDs
- speaking file list

Adding a new mock must not break export compatibility.

## Validation

After creating a new full mock, the agent must run:

```sh
python3 tools/validate_data.py
```

The task is not complete until the validator passes.

The agent must also manually confirm:

1. Reading item count = 50
2. Listening item count = 47
3. Writing item count = 12
4. Speaking item count = 11
5. Reading duration = 30
6. Listening duration = 29
7. Writing duration = 23
8. Speaking duration = 8
9. No duplicate question IDs
10. No missing referenced question IDs
11. No JSON parse errors
12. Complete the Words underscore/answer lengths match
13. No duplicate question references inside the same mock
14. Export compatibility is intact

## Agent Workflow

An agent creating a new full mock should follow this order:

1. Read `AGENT_DATA_CONTRACT.md`.
2. Read `references/FULL_MOCK_CREATION.md`.
3. Read the relevant style files under `references/` for each question type.
4. Inspect current `data/questions.json` content and existing mocks.
5. Check previously used question IDs.
6. Generate new questions if needed.
7. Create a new mock ID.
8. Add the mock definition to `data/tests.json`.
9. Run the validator.
10. Report the results.

## Delivery Report

When a new mock is complete, report this table:

| Section | Item Count | Duration |
| --- | ---: | ---: |
| Reading | 50 | 30 min |
| Listening | 47 | 29 min |
| Writing | 12 | 23 min |
| Speaking | 11 | 8 min |

Also report task-type distribution.

Example:

Reading:

- Complete the Words: X
- Read in Daily Life: X
- Academic Passage: X

Listening:

- Choose a Response: X
- Conversation: X
- Announcement: X
- Academic Talk: X

Writing:

- Build a Sentence: X
- Email: 1
- Academic Discussion: 1

Speaking:

- Listen and Repeat: X
- Take an Interview: X

Do not present subtask distributions as official exact ETS distributions.

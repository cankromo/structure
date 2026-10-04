# Agent Data Contract

This project is maintained by agents, not by the admin UI. Treat this file as the source of truth when adding practice questions or full mock tests.

## Files

- `data/questions.json` is the shared question bank for practice and mock tests.
- `data/tests.json` defines full mock tests by referencing question IDs from `data/questions.json`.
- `practice/index.html` automatically shows every item in `data/questions.json` by question type.
- `mock/index.html` only shows tests listed in `data/tests.json`.

## Question Types

Use these exact top-level keys in `data/questions.json`:

- `complete_words`
- `daily_life`
- `academic_passage`
- `choose_response`
- `conversations`
- `announcements`
- `academic_talks`
- `build_sentence`
- `email`
- `discussion`
- `repeat`
- `interview`

## ID Rules

- Never change or reuse an existing ID.
- Use stable prefixes:
  - `cw_` for Complete the Words
  - `rdl_` for Read in Daily Life
  - `rap_` for Academic Passage
  - `lcr_` for Listen and Choose a Response
  - `conv_` for Conversation
  - `ann_` for Announcement
  - `talk_` for Academic Talk
  - `bs_` for Build a Sentence
  - `we_` for Write an Email
  - `ad_` for Academic Discussion
  - `rep_` for Listen and Repeat
  - `int_` for Interview
- For a new full mock, use a new numeric range. Example: `mock_003` should normally use `*_301`, `*_302`, etc.
- Do not reuse the same question ID inside one mock.

## Full Mock Standard

Every full mock test must use this section order:

1. Reading
2. Listening
3. Writing
4. Speaking

Every full mock test must use these durations:

- Reading: 30 minutes
- Listening: 29 minutes
- Writing: 23 minutes
- Speaking: 8 minutes

Every full mock test must have these exact item totals:

- Reading: 50 items
- Listening: 47 items
- Writing: 12 items
- Speaking: 11 items

Current non-official internal distribution used by the project:

- Reading: Complete Words 20, Daily Life 12, Academic Passage 18
- Listening: Choose Response 12, Conversations 16, Announcements 9, Academic Talks 10
- Writing: Build Sentence 10, Email 1, Discussion 1
- Speaking: Repeat 6, Interview 5

Do not label this distribution as official ETS distribution.

## Item Counting Rules

- `complete_words`: each blank is one item, counted from `answers.length`.
- `daily_life`, `academic_passage`, `conversations`, `announcements`, `academic_talks`: each nested question is one item.
- `choose_response`, `build_sentence`, `email`, `discussion`, `repeat`, `interview`: each object is one item.

## Content References

- Before creating a new full mock, read `references/FULL_MOCK_CREATION.md` and follow its validation and quality rules.
- Before generating Complete the Words items, read `references/COMPLETE_WORDS_STYLE.md`.
- Before generating Read in Daily Life items, read `references/READ_IN_DAILY_LIFE_STYLE.md`.
- Do not add new questions unless the content follows the quality rules in the relevant reference file.

## Schema Rules

Complete Words:

- `text` contains visible word prefixes followed by underscores.
- The first sentence should be complete.
- Each underscore run must match the corresponding answer length exactly.
- `answers` contain only the missing letters, not the full word.

Multiple-choice reading/listening types:

- Each question has `q`, `options`, and numeric `answer`.
- `answer` is zero-based and must point to an existing option.

Conversations:

- Use `turns` as `[speaker, text]` pairs.
- Use speaker labels such as `Student`, `Advisor`, `Professor`, `Staff Member`, `Librarian`, or `Producer`.

Build a Sentence:

- `parts` must already be in the correct order.
- The UI shuffles display order and checks the selected order against `parts`.

Writing:

- `email` objects use `prompt`.
- `discussion` objects use `prompt`.

Speaking:

- `repeat` objects use `text`.
- `interview` objects use `prompt`.

## Required Agent Workflow

Before editing:

1. Read `AGENT_DATA_CONTRACT.md`.
2. Inspect current max IDs in `data/questions.json`.
3. Pick a new unused numeric range.

When adding a full mock:

1. Add all new question objects to `data/questions.json`.
2. Add one new `mock_###` object to `data/tests.json`.
3. Reference only IDs that exist in `data/questions.json`.
4. Do not reuse old demo/mock IDs unless explicitly requested.
5. Run `python3 tools/validate_data.py`.

When adding practice-only questions:

1. Add the new question objects to `data/questions.json`.
2. Do not add them to `data/tests.json` unless they belong to a mock.
3. Run `python3 tools/validate_data.py`.

## Validation

Run:

```sh
python3 tools/validate_data.py
```

The validation must pass before handing work back.

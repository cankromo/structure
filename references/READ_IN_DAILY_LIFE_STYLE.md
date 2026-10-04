# Read in Daily Life Style Reference

This file defines the content standard for future agents generating `daily_life` items. It is based on observed ETS/Flex Practice-style task patterns and is a style reference only. New content must be fully original.

## Task Title

Use this task concept:

```text
Read in Daily Life
```

## Screen Logic

The task shows a short real-life text that a user could plausibly encounter. One common format is an email.

Typical screen logic:

- The text or document appears on the left.
- A single multiple-choice question appears on the right.
- There are 4 answer options.
- The same text may be used for more than one question.
- Later questions on the same text should measure a different skill.

This file does not require copying the UI exactly. The important standards are text type, question logic, difficulty, distractor quality, and same-passage multi-question structure.

## Common Question Types

### A. Main Purpose / Gist

Example wording:

```text
What is the main purpose of the email?
```

Expected skill:

- Identify the overall communication purpose.
- Distractors may use details from the text, but those details should not be the main purpose.

### B. Main Topic / What Is Being Communicated

Example wording:

```text
What is the company informing employees about?
```

Expected skill:

- Identify the central topic of a notice, message, or email.
- Suitable content includes office relocation, schedule changes, event notices, and similar everyday communications.

### C. Inference

Example wording:

```text
What can be inferred about Professor Nagasu?
```

Expected skill:

- The correct answer may not be copied word-for-word from the text.
- The answer must be safely supported by the text.
- The inference must not be speculative.

### D. Conclusion About a Referenced Item

Example wording:

```text
What can be concluded about The Hidden Path?
```

Expected skill:

- Draw a supported conclusion about a named book, event, person, service, object, or similar referenced item.

## Reference Text Patterns

Observed example-style structures include:

1. Book club email:
   - meeting date/time change
   - venue information
   - parking warning
   - discussion book
   - extra instructions
   - sample skill: conclude something about a specific book

2. Company relocation email:
   - move date
   - new facility
   - IT readiness
   - parking or address update
   - sample skill: identify what employees are being informed about

3. Internship offer email:
   - candidate selected
   - background praised
   - professor reference
   - start date, office, required documents
   - sample skill 1: identify the main purpose of the email
   - sample skill 2: infer something about a professor

## Content Standard

- Text must be natural English that could appear in real life.
- Suitable formats include:
  - email
  - notice
  - message
  - announcement
  - schedule
  - memo
  - event information
  - workplace communication
  - campus communication
- Text should usually be short and functional.
- Target difficulty should be around B2-C1.
- Avoid unnecessary academic jargon.
- Questions should not be simple word hunts.
- A set should include a mix of main idea, detail, and inference questions.
- The correct option must be unique and clearly defensible.
- Distractors should be plausible.
- Distractors may be based on real information from the text, but must differ clearly from the correct answer.
- Do not write obviously silly distractors.
- The answer must not require outside world knowledge.
- If one passage has 2 or more questions, the questions must not ask the same thing twice.
- One question may test main purpose while another tests inference or detail.
- Do not copy real ETS questions.
- Use examples only as references for style, length, and question type.

## Quality Checks

Before adding a `daily_life` item:

- Confirm the passage has a realistic communicative purpose.
- Confirm every question is answerable from the passage.
- Confirm there are exactly 4 options per question.
- Confirm the zero-based `answer` index points to the correct option.
- Confirm distractors are plausible but not equally correct.
- Confirm multi-question sets test different skills.

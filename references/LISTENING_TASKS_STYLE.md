# Listening Tasks Style Reference

This file defines shared content standards for TOEFL-style Listening practice and full mock items in this repo.

## Covered Task Types

Use this reference before generating:

- `choose_response` — Listen and Choose a Response
- `conversations` — Listen to a Conversation
- `announcements` — Listen to an Announcement
- `academic_talks` — Listen to an Academic Talk

## Global Listening Rules

- Listening scripts should be heard, not shown to the user during normal practice or mock mode.
- Audio should use the existing `SpeechSynthesis` / Mac voice-selection system.
- Only one audio item should play at a time.
- If the current UI uses play-once behavior, preserve it.
- For multi-question conversations and announcements, each question may provide its own play button so the same audio can be heard again for that question.
- Do not make distractors silly or obviously unrelated.
- Correct answers should be distributed across answer positions over a large set.

## Listen and Choose a Response

Pattern:

- The user hears one short spoken sentence or question.
- The user selects the most appropriate response.

Quality rules:

- Keep prompts short and natural.
- Use everyday academic, campus, workplace, service, or social situations.
- Test pragmatic fit, not only literal word matching.
- Include plausible but pragmatically wrong responses.
- Avoid obscure idioms or slang.

## Listen to a Conversation

Before generating this task type, also read `references/CONVERSATION_STYLE.md`.

Pattern:

- A short conversation between two speakers.
- Common roles: student, advisor, professor, staff member, librarian, producer, or campus employee.
- Multiple questions may follow one conversation.

Quality rules:

- Use distinct speaker voices rather than announcing speaker names aloud.
- Keep turns natural and purposeful.
- Questions may test gist, detail, inference, purpose, attitude, and function.
- The conversation should contain enough context for all answers.
- Do not ask several questions that measure the same detail.

## Listen to an Announcement

Pattern:

- A short spoken notice from a campus, workplace, museum, library, event, transit, or service setting.
- Multiple questions may follow one announcement.

Quality rules:

- Include concrete details such as time, place, reason, change, requirement, or next step.
- Questions should mix main message, detail, purpose, and inference.
- Use a natural announcer voice and moderate rate.
- Avoid overloading the script with unnecessary numbers.

## Listen to an Academic Talk

Before generating this task type, also read `references/ACADEMIC_TALK_STYLE.md`.

Pattern:

- A short academic mini-lecture or classroom explanation.
- Multiple questions may follow one talk.

Quality rules:

- Use university-level but accessible topics.
- Include clear organization: topic, explanation, example, implication.
- Questions should mix main idea, detail, inference, purpose, vocabulary/function, and example purpose.
- Use a lecturer voice and slightly slower rate than casual dialogue.
- Avoid scripts that are too short to support multiple questions.

## Storage Policy

Generated listening items should go in `data/questions.json` only when explicitly requested. Raw official/user-provided samples, if any, should remain under `references/raw_official_samples/` and must not be copied into public generated content.


# Academic Discussion Writing Style Reference

This file defines the content standard for future agents generating `discussion` items. It is based on user-provided official TOEFL training samples kept under `references/raw_official_samples/academic_discussion/`. Do not copy official prompts into new public practice content. Use these samples only to understand format, task logic, difficulty, and discussion design.

## Task Identity

This task is the TOEFL-style academic writing discussion task. In the current repo schema, generated items belong under:

```json
{
  "discussion": [
    {
      "id": "ad_###",
      "prompt": "..."
    }
  ]
}
```

## Core Structure

A strong Academic Discussion prompt should include:

- A short course context.
- A professor name.
- A professor question that asks for an opinion.
- Two student posts with different or partially conflicting views.
- Instructions requiring the test taker to express and support an opinion.
- A clear expectation that an effective response is at least 100 words.

Typical framing:

- The professor is teaching a class in a field such as sociology, business, marketing, tourism management, labor studies, child development, or student orientation.
- The professor asks a debatable but accessible question.
- The two student posts model different angles, not complete answers that exhaust the topic.

## Prompt Design Rules

The professor question should:

- Be understandable without specialized background knowledge.
- Ask for a clear opinion or judgment.
- Invite explanation, examples, and comparison.
- Be broad enough for a 100+ word response but narrow enough to stay focused.
- Avoid requiring personal disclosure that is too sensitive.
- Avoid topics that depend on current news or unstable facts.

Good professor questions often ask:

- whether a goal is worthwhile
- which factor is most important
- whether a technology or practice is beneficial
- why a social or business strategy works
- what policy or solution would be best

## Student Post Rules

Each prompt should include two student posts.

The posts should:

- Be written in natural student-like English.
- Be around 45-80 words each.
- Offer concrete reasons or examples.
- Give the test taker something to agree with, disagree with, qualify, or extend.
- Represent distinct perspectives.

The posts should not:

- Sound like perfect essays.
- Fully answer every possible angle.
- Use overly technical vocabulary.
- Be silly or obviously weak.
- Repeat the professor question without adding a viewpoint.

## Difficulty and Language

Target difficulty should be B2-C1.

Use:

- clear academic classroom language
- everyday university topics
- concrete examples
- manageable sentence complexity

Avoid:

- C2 or expert-only vocabulary
- highly specialized academic theories
- culture-specific knowledge that would disadvantage test takers
- controversial issues that require outside factual knowledge

## Topic Patterns

Suitable topic areas include:

- sociology and leisure
- student course selection
- marketing and advertising
- work trends and retirement
- management qualities
- tourism and crowd control
- child development and technology
- entrepreneurship
- remote work and workplace culture
- education policy
- campus life
- public communication
- community planning

## Quality Checks

Before adding a new `discussion` item:

- Confirm the task asks for an opinion.
- Confirm both student posts are relevant and distinct.
- Confirm the test taker can contribute a new idea, not just repeat a student.
- Confirm the prompt can be answered in at least 100 words.
- Confirm the language is B2-C1 and not too technical.
- Confirm the prompt is fully original.
- Confirm the generated content does not copy official sample wording.

## Good Example Traits

Good generated prompts:

- State a realistic course context.
- Present a professor question with a clear choice or evaluative angle.
- Include two student responses that create a useful discussion space.
- Let the test taker agree, disagree, synthesize, or add a third perspective.
- Encourage reasoning rather than personal storytelling only.

## Bad Example Traits

Avoid prompts that:

- Ask a yes/no question without room for reasoning.
- Have two student posts that say essentially the same thing.
- Make one student post obviously correct and the other obviously ridiculous.
- Require expert knowledge or external statistics.
- Copy or lightly paraphrase official TOEFL training samples.
- Ask for fewer than 100 words or omit the discussion contribution requirement.

## Storage Policy

Official/user-provided samples should stay in:

```text
references/raw_official_samples/academic_discussion/
```

Generated practice questions should go in `data/questions.json` only when explicitly requested, and must be original.

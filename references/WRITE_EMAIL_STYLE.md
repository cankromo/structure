# Write an Email Style Reference

This file defines the content standard for future agents generating `email` items. It is based on user-provided TOEFL-style writing samples kept under `references/raw_official_samples/write_email/`. Do not copy official prompts into new public practice content. Use the samples only to understand format, task logic, difficulty, and prompt design.

## Task Identity

This task is the TOEFL-style Write an Email task. In the current repo schema, generated items belong under:

```json
{
  "email": [
    {
      "id": "we_###",
      "prompt": "..."
    }
  ]
}
```

## Core Structure

A strong Write an Email prompt should include:

- A realistic situation, often 2-4 sentences.
- A named or clearly defined recipient.
- A clear reason for writing.
- The exact instruction frame: `Write an email to [recipient]. In your email, do the following.`
- Three separate content requirements, each on its own line.
- The sentence: `Write as much as you can and in complete sentences.`
- A `Your Response:` line.
- Visible `To:` and `Subject:` lines.

Typical task flow:

1. Describe the situation.
2. Tell the test taker who to email.
3. Introduce the three requirements with `In your email, do the following.`
4. Give three concrete things the email must do, one per line.
5. Ask the test taker to write as much as possible in complete sentences.
6. Provide `Your Response:`, `To:`, and `Subject:` starter lines.

Recommended prompt template:

```text
You are ...
You need to ...

Write an email to [recipient]. In your email, do the following.
[Requirement 1]
[Requirement 2]
[Requirement 3]
Write as much as you can and in complete sentences.

Your Response:

To: [recipient]
Subject: [short subject]
```

## Common Scenario Types

Suitable scenarios include:

- planning a trip or event with a friend
- organizing club members for a performance or project
- coordinating travel details
- reporting a service problem
- asking a relative or friend for help
- requesting support from a company, office, or staff member
- proposing plans and asking for feedback

The scenario should be everyday and practical. It should not require specialized knowledge.

## Requirement Design

Each prompt should have exactly three main content requirements.

Good requirements ask the test taker to:

- suggest or describe a plan
- explain why something is a good choice
- describe needed items, tasks, or problems
- ask for help
- request a solution
- suggest a meeting time
- ask for the recipient's opinion

The three requirements should be distinct. Do not ask the same thing in three different ways.

## Recipient and Tone

Recipient type determines tone:

- Friend or family member: friendly but organized.
- Club members or classmates: semi-formal and practical.
- Customer service or university staff: polite and formal.

The prompt should make the relationship clear enough for the test taker to choose an appropriate tone.

## Difficulty and Language

Target difficulty should be B1-B2+ for the prompt itself, while allowing B2-C1 responses.

Use:

- clear everyday English
- concrete details
- realistic constraints
- complete but concise instructions

Avoid:

- obscure topics
- emotionally sensitive personal crises
- overly complex institutional procedures
- prompts requiring outside factual knowledge
- impossible or conflicting requirements

## Quality Checks

Before adding a new `email` item:

- Confirm the recipient is clear.
- Confirm the situation is realistic.
- Confirm there are exactly three distinct content requirements.
- Confirm the three requirements appear as separate instruction lines.
- Confirm `Your Response:`, `To:`, and `Subject:` are included.
- Confirm the requirements naturally fit into one email.
- Confirm the test taker can answer without outside knowledge.
- Confirm the prompt is fully original.
- Confirm it does not copy or lightly paraphrase official samples.

## Good Example Traits

Good generated prompts:

- Give enough context to write immediately.
- Include a practical purpose.
- Ask for explanation, description, and request/action.
- Make the recipient relationship clear.
- Support complete-sentence writing.

## Bad Example Traits

Avoid prompts that:

- Only ask for one action.
- Include too many tasks to handle in a short email.
- Make the relationship to the recipient unclear.
- Require technical expertise.
- Use vague requirements such as "write about the issue" without specifying what to include.
- Copy official TOEFL training sample wording.

## Storage Policy

Official/user-provided samples should stay in:

```text
references/raw_official_samples/write_email/
```

Generated practice questions should go in `data/questions.json` only when explicitly requested, and must be original.

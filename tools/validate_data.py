#!/usr/bin/env python3
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTIONS_PATH = ROOT / "data" / "questions.json"
TESTS_PATH = ROOT / "data" / "tests.json"

QUESTION_TYPES = {
    "complete_words",
    "daily_life",
    "academic_passage",
    "choose_response",
    "conversations",
    "announcements",
    "academic_talks",
    "build_sentence",
    "email",
    "discussion",
    "repeat",
    "interview",
}

EXPECTED_DURATIONS = {
    "reading": 30,
    "listening": 29,
    "writing": 23,
    "speaking": 8,
}

EXPECTED_COUNTS = {
    "reading": 50,
    "listening": 47,
    "writing": 12,
    "speaking": 11,
}

EXPECTED_SPEAKING_DISTRIBUTION = {
    "repeat": 7,
    "interview": 4,
}

SECTION_ORDER = ["reading", "listening", "writing", "speaking"]


def load_json(path):
    with path.open() as file:
        return json.load(file)


def item_count(question_type, item):
    if question_type == "complete_words":
        return len(item.get("answers", []))
    if question_type in {
        "daily_life",
        "academic_passage",
        "conversations",
        "announcements",
        "academic_talks",
    }:
        return len(item.get("questions", []))
    return 1


def validate_questions(questions):
    errors = []

    missing_types = sorted(QUESTION_TYPES - set(questions))
    extra_types = sorted(set(questions) - QUESTION_TYPES)
    if missing_types:
        errors.append(f"Missing question type keys: {', '.join(missing_types)}")
    if extra_types:
        errors.append(f"Unknown question type keys: {', '.join(extra_types)}")

    all_ids = []
    for question_type, items in questions.items():
        if not isinstance(items, list):
            errors.append(f"{question_type} must be a list")
            continue
        for item in items:
            item_id = item.get("id")
            if not item_id:
                errors.append(f"{question_type} item missing id")
                continue
            all_ids.append(item_id)
            errors.extend(validate_item(question_type, item))

    duplicates = sorted(item_id for item_id, count in Counter(all_ids).items() if count > 1)
    if duplicates:
        errors.append(f"Duplicate question IDs: {', '.join(duplicates)}")

    return errors


def validate_item(question_type, item):
    errors = []
    item_id = item.get("id", "<missing id>")

    if question_type == "complete_words":
        text = item.get("text", "")
        answers = item.get("answers", [])
        blanks = re.findall(r"[A-Za-z]+(_+)", text)
        if len(blanks) != len(answers):
            errors.append(
                f"{item_id}: blank count {len(blanks)} does not match answers {len(answers)}"
            )
        for index, (blank, answer) in enumerate(zip(blanks, answers), 1):
            if len(blank) != len(answer):
                errors.append(
                    f"{item_id}: blank {index} length {len(blank)} does not match answer '{answer}' length {len(answer)}"
                )

    if question_type in {
        "daily_life",
        "academic_passage",
        "conversations",
        "announcements",
        "academic_talks",
    }:
        for index, question in enumerate(item.get("questions", []), 1):
            errors.extend(validate_mc_question(item_id, index, question))

    if question_type == "choose_response":
        errors.extend(validate_mc_question(item_id, 1, item))

    if question_type == "conversations":
        turns = item.get("turns", [])
        if not turns:
            errors.append(f"{item_id}: conversation missing turns")
        for turn_index, turn in enumerate(turns, 1):
            if not isinstance(turn, list) or len(turn) != 2:
                errors.append(f"{item_id}: turn {turn_index} must be [speaker, text]")

    if question_type == "build_sentence" and not item.get("parts"):
        errors.append(f"{item_id}: build_sentence missing parts")

    if question_type in {"email", "discussion", "interview"} and not item.get("prompt"):
        errors.append(f"{item_id}: missing prompt")

    if question_type == "repeat" and not item.get("text"):
        errors.append(f"{item_id}: missing text")

    return errors


def validate_mc_question(item_id, index, question):
    errors = []
    options = question.get("options", [])
    answer = question.get("answer")
    if not question.get("q") and "prompt" not in question:
        errors.append(f"{item_id}: question {index} missing q/prompt")
    if not isinstance(options, list) or len(options) < 2:
        errors.append(f"{item_id}: question {index} needs at least two options")
    if not isinstance(answer, int) or answer < 0 or answer >= len(options):
        errors.append(f"{item_id}: question {index} answer index out of range")
    return errors


def validate_tests(questions, tests):
    errors = []
    by_type = {
        question_type: {item["id"]: item for item in items}
        for question_type, items in questions.items()
    }

    if "tests" not in tests or not isinstance(tests["tests"], list):
        return ["tests.json must contain a tests list"]

    test_ids = [test.get("id") for test in tests["tests"]]
    duplicate_tests = sorted(test_id for test_id, count in Counter(test_ids).items() if count > 1)
    if duplicate_tests:
        errors.append(f"Duplicate test IDs: {', '.join(duplicate_tests)}")

    for test in tests["tests"]:
        test_id = test.get("id", "<missing test id>")
        durations = test.get("durations", {})
        if durations != EXPECTED_DURATIONS:
            errors.append(f"{test_id}: durations must be {EXPECTED_DURATIONS}")

        sections = test.get("sections", {})
        if list(sections.keys()) != SECTION_ORDER:
            errors.append(f"{test_id}: section order must be {', '.join(SECTION_ORDER)}")

        used_ids = []
        section_counts = {}
        distribution = defaultdict(dict)

        for section_name in SECTION_ORDER:
            total = 0
            for group in sections.get(section_name, []):
                question_type = group.get("type")
                ids = group.get("ids", [])
                subtotal = 0
                for question_id in ids:
                    used_ids.append(question_id)
                    item = by_type.get(question_type, {}).get(question_id)
                    if item is None:
                        errors.append(f"{test_id}: missing referenced ID {question_id} in {question_type}")
                        continue
                    subtotal += item_count(question_type, item)
                distribution[section_name][question_type] = subtotal
                total += subtotal
            section_counts[section_name] = total

        for section_name, expected_count in EXPECTED_COUNTS.items():
            if section_counts.get(section_name) != expected_count:
                errors.append(
                    f"{test_id}: {section_name} count {section_counts.get(section_name)} must be {expected_count}"
                )

        speaking_distribution = distribution.get("speaking", {})
        for question_type, expected_count in EXPECTED_SPEAKING_DISTRIBUTION.items():
            if speaking_distribution.get(question_type) != expected_count:
                errors.append(
                    f"{test_id}: speaking {question_type} count {speaking_distribution.get(question_type)} must be {expected_count}"
                )

        duplicate_used = sorted(item_id for item_id, count in Counter(used_ids).items() if count > 1)
        if duplicate_used:
            errors.append(f"{test_id}: duplicate referenced IDs: {', '.join(duplicate_used)}")

        print(f"{test_id}: counts={section_counts} distribution={dict(distribution)}")

    return errors


def main():
    questions = load_json(QUESTIONS_PATH)
    tests = load_json(TESTS_PATH)

    errors = []
    errors.extend(validate_questions(questions))
    errors.extend(validate_tests(questions, tests))

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("Validation passed.")


if __name__ == "__main__":
    main()

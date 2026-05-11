#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / "src"
ROOT_README = ROOT / "README.md"
SRC_README = SRC_DIR / "README.md"
ROOT_MARKER_START = "<!-- GENERATED:ROOT:START -->"
ROOT_MARKER_END = "<!-- GENERATED:ROOT:END -->"
SRC_MARKER_START = "<!-- GENERATED:SRC:START -->"
SRC_MARKER_END = "<!-- GENERATED:SRC:END -->"
REQUIRED_FIELDS = ("id", "title", "difficulty", "time", "space")
HELPER_FILES = {"ListNode.java", "TreeNode.java"}

TOPIC_DESCRIPTIONS = {
    "arrays_hashing": "Foundations of data storage and retrieval.",
    "binary_search": "Efficient searching in sorted datasets.",
    "binary_trees": "Recursive (DFS) and iterative (BFS) traversal techniques.",
    "linked_lists": "Manual pointer manipulation and in-place operations.",
    "sliding_window": "Subarray optimization and string analysis.",
    "stacks": "LIFO logic for nested structures.",
    "two_pointers": "Space-efficient array traversals.",
}


@dataclass(frozen=True)
class Problem:
    problem_id: int
    title: str
    difficulty: str
    time_complexity: str
    space_complexity: str
    topic: str
    path: Path


HEADER_PATTERN = re.compile(r"/\*\*(.*?)\*/", re.DOTALL)
FIELD_PATTERN = re.compile(r"@lc\s+([a-z]+)=(.+)")


def main() -> int:
    problems = collect_problems()
    write_readme(
        ROOT_README,
        ROOT_MARKER_START,
        ROOT_MARKER_END,
        build_root_section(problems),
    )
    write_readme(
        SRC_README,
        SRC_MARKER_START,
        SRC_MARKER_END,
        build_src_section(problems),
    )
    return 0


def collect_problems() -> list[Problem]:
    problems: list[Problem] = []
    for java_file in sorted(SRC_DIR.rglob("*.java")):
        if java_file.name in HELPER_FILES:
            continue
        problems.append(parse_problem(java_file))

    if not problems:
        raise SystemExit("No LeetCode solution files were found under src/.")

    duplicate_ids = [
        problem_id
        for problem_id, count in Counter(problem.problem_id for problem in problems).items()
        if count > 1
    ]
    if duplicate_ids:
        duplicates = ", ".join(str(problem_id) for problem_id in sorted(duplicate_ids))
        raise SystemExit(f"Duplicate LeetCode ids found: {duplicates}")

    return sorted(problems, key=lambda problem: problem.problem_id)


def parse_problem(java_file: Path) -> Problem:
    content = java_file.read_text(encoding="utf-8")
    header_match = HEADER_PATTERN.search(content)
    if not header_match:
        raise SystemExit(f"Missing @lc metadata header in {java_file.relative_to(ROOT)}")

    fields: dict[str, str] = {}
    for raw_line in header_match.group(1).splitlines():
        line = raw_line.strip(" *")
        field_match = FIELD_PATTERN.fullmatch(line)
        if field_match:
            fields[field_match.group(1)] = field_match.group(2).strip()

    missing_fields = [field for field in REQUIRED_FIELDS if field not in fields]
    if missing_fields:
        missing = ", ".join(missing_fields)
        raise SystemExit(
            f"Incomplete @lc metadata header in {java_file.relative_to(ROOT)}: missing {missing}"
        )

    try:
        problem_id = int(fields["id"])
    except ValueError as exc:
        raise SystemExit(
            f"Invalid @lc id in {java_file.relative_to(ROOT)}: {fields['id']}"
        ) from exc

    return Problem(
        problem_id=problem_id,
        title=fields["title"],
        difficulty=fields["difficulty"],
        time_complexity=fields["time"],
        space_complexity=fields["space"],
        topic=java_file.parent.name,
        path=java_file.relative_to(ROOT),
    )


def build_root_section(problems: list[Problem]) -> str:
    difficulty_counts = Counter(problem.difficulty for problem in problems)
    topic_counts = Counter(problem.topic for problem in problems)

    lines = [
        "## 📊 Problem Tracking",
        "",
        f"- **Total solved:** {len(problems)}",
        f"- **Difficulty breakdown:** Easy {difficulty_counts.get('Easy', 0)}, Medium {difficulty_counts.get('Medium', 0)}, Hard {difficulty_counts.get('Hard', 0)}",
        f"- **Topics covered:** {format_topic_counts(topic_counts)}",
        "",
        "| # | Problem | Difficulty | Topic | Time Complexity | Space Complexity |",
        "| :--- | :--- | :--- | :--- | :--- | :--- |",
    ]

    for problem in problems:
        lines.append(
            "| {problem_id} | {title} | {difficulty} | `{topic}` | ${time}$ | ${space}$ |".format(
                problem_id=problem.problem_id,
                title=problem.title,
                difficulty=problem.difficulty,
                topic=problem.topic,
                time=escape_markdown_math(problem.time_complexity),
                space=escape_markdown_math(problem.space_complexity),
            )
        )

    return "\n".join(lines)


def build_src_section(problems: list[Problem]) -> str:
    topic_counts = Counter(problem.topic for problem in problems)
    lines = [
        "### 🛠 Directory Structure",
        "",
        "| Directory | Problems | Notes |",
        "| :--- | ---: | :--- |",
    ]

    for topic in sorted(topic_counts):
        lines.append(
            "| `{topic}/` | {count} | {description} |".format(
                topic=topic,
                count=topic_counts[topic],
                description=TOPIC_DESCRIPTIONS.get(topic, "LeetCode solutions."),
            )
        )

    return "\n".join(lines)


def format_topic_counts(topic_counts: Counter[str]) -> str:
    return ", ".join(
        f"`{topic}` {topic_counts[topic]}" for topic in sorted(topic_counts)
    )


def escape_markdown_math(value: str) -> str:
    return value.replace("\\", "\\\\")


def write_readme(path: Path, start_marker: str, end_marker: str, generated_section: str) -> None:
    content = path.read_text(encoding="utf-8")
    updated = replace_between_markers(content, start_marker, end_marker, generated_section)
    path.write_text(updated, encoding="utf-8")


def replace_between_markers(content: str, start_marker: str, end_marker: str, generated: str) -> str:
    if start_marker not in content or end_marker not in content:
        raise SystemExit(f"Missing generated markers in {start_marker} / {end_marker}")

    pattern = re.compile(
        re.escape(start_marker) + r".*?" + re.escape(end_marker),
        re.DOTALL,
    )
    replacement = f"{start_marker}\n{generated}\n{end_marker}"
    return pattern.sub(replacement, content, count=1)


if __name__ == "__main__":
    sys.exit(main())

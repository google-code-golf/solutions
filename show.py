#!/usr/bin/env python3

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import sys

from blessed import Terminal


@dataclass(frozen=True, slots=True)
class TestCase:
    input: list[list[int]]
    output: list[list[int]]

    @staticmethod
    def from_dict(data: dict) -> TestCase:
        return TestCase(data["input"], data["output"])


@dataclass(frozen=True, slots=True)
class Task:
    train: list[TestCase]
    test: list[TestCase]
    arc_gen: list[TestCase]

    def all(self) -> list[tuple[str, TestCase]]:
        examples = []
        for i, testcase in enumerate(self.train):
            examples.append((f"Train {i + 1}", testcase))
        for i, testcase in enumerate(self.test):
            examples.append((f"Test {i + 1}", testcase))
        for i, testcase in enumerate(self.arc_gen):
            examples.append((f"ARC-Gen {i + 1}", testcase))
        return examples

    @staticmethod
    def from_dict(data: dict) -> Task:
        train = [TestCase.from_dict(tc) for tc in data["train"]]
        test = [TestCase.from_dict(tc) for tc in data["test"]]
        arc_gen = [TestCase.from_dict(tc) for tc in data.get("arc-gen", [])]
        return Task(train, test, arc_gen)

    @staticmethod
    def load(task_num: int) -> Task:
        task_filename = f"task{task_num:03d}.json"
        task_path = Path("tasks") / task_filename
        with open(task_path) as f:
            task_data = json.load(f)
        return Task.from_dict(task_data)


def print_matrix(term: Terminal, matrix: list[list[int]]) -> None:
    colours = {
        0: term.on_gray20,
        1: term.on_blue,
        2: term.on_red,
        3: term.on_green,
        4: term.on_yellow,
        5: term.on_gray50,
        6: term.on_magenta,
        7: term.on_orange3,
        8: term.on_cyan,
        9: term.on_maroon,
    }

    for row in matrix:
        for val in row:
            num = f"{val:2}" if val != 0 else "  "
            color = colours.get(val, term.on_white)
            print(color(num), end="")
        print()


def show_testcase(
    term: Terminal, testcase: TestCase, label: str, current: int, total: int
) -> None:
    print(term.clear())
    print("j ← → k, q = quit")
    print()
    print(term.bold_underline(f"{label}") + f" ({current + 1}/{total})")
    print()
    print(f"Input ({len(testcase.input)}x{len(testcase.input[0])}):")
    print()
    print_matrix(term, testcase.input)
    print()
    print(f"Output ({len(testcase.output)}x{len(testcase.output[0])}):")
    print()
    print_matrix(term, testcase.output)
    print()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python show.py <task_num>")
        sys.exit(1)

    task_num = int(sys.argv[1])
    task = Task.load(task_num)
    term = Terminal()
    examples = task.all()
    i = 0

    try:
        with term.cbreak(), term.hidden_cursor():
            while True:
                label, testcase = examples[i]
                show_testcase(term, testcase, label, i, len(examples))

                key = term.inkey()

                if key == "j" or key.name == "KEY_LEFT":
                    i = (i - 1) % len(examples)
                elif key == "k" or key.name == "KEY_RIGHT":
                    i = (i + 1) % len(examples)
                elif key == "q":
                    break
    except KeyboardInterrupt:
        pass
    finally:
        print(term.clear())


if __name__ == "__main__":
    main()

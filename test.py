import argparse
import copy
from multiprocessing import Pool, cpu_count
import os
from pathlib import Path
import sys
import time
import warnings

from common import Task, load_solution

import numpy as np

TASKS = Path("tasks")


def test_task(args):
    task_num, solutions_dir = args
    start_time = time.time()

    task = Task.load(task_num, TASKS)
    module = load_solution(task_num, solutions_dir)
    p = getattr(module, "p")

    path = solutions_dir / f"task{task_num:03d}.py"

    passed = total = 0
    for testcase in task.all_testcases():
        total += 1
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                input_copy = copy.deepcopy(testcase.input)
                output = p(input_copy)
                if np.array_equal(np.array(output), np.array(testcase.output)):
                    passed += 1
        except Exception:
            pass

    return task_num, passed == total, os.path.getsize(path)


def main():
    parser = argparse.ArgumentParser(description="Test solutions")
    parser.add_argument(
        "tasks", nargs="*", type=int, help="Task numbers (default: all)"
    )
    parser.add_argument(
        "-j", "--jobs", type=int, default=cpu_count(), help="Worker count"
    )
    parser.add_argument(
        "-d",
        "--directory",
        type=str,
        default="build",
        help="Solutions directory (default: build)",
    )
    args = parser.parse_args()

    solutions_dir = Path(args.directory)
    tasks: list[int] = args.tasks or [*range(1, 401)]

    tasks_list = [(task_num, solutions_dir) for task_num in tasks]
    with Pool(args.jobs) as pool:
        results = []
        total = len(tasks_list)
        completed_tasks = set()
        for i, r in enumerate(pool.imap_unordered(test_task, tasks_list), 1):
            if r:
                results.append(r)
                task_num, ok, bytes_count = r
                completed_tasks.add(task_num)
                status = "✓" if ok else "✘"
                print(
                    f"\r[{i}/{total}] task{task_num:03d}: {status} {bytes_count}b"
                    + " " * 20
                )

                pending = [t for t, _ in tasks_list if t not in completed_tasks]
                if pending:
                    print(
                        f"Pending: {pending[:20]}{'...' if len(pending) > 20 else ''}"
                    )
        print()

    print(f"\n{'Task':<7}  {'Result':<8}  {'Bytes':<8}")
    print("-" * 28)

    ok_count = sum(ok for _, ok, _ in results)
    total_bytes = sum(bytes_count for _, _, bytes_count in results)

    for task_num, ok, bytes_count in results[:10]:
        status = "✓" if ok else "✘"
        print(f"task{task_num:03d}  {status:<8}  {bytes_count:<8}")

    print("-" * 28)
    print(f"Passed: {ok_count}/{len(results)}")
    print(f"Total bytes: {total_bytes}")

    if ok_count < len(results):
        sys.exit(1)


if __name__ == "__main__":
    main()

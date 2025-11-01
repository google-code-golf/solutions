import os
import sys
from pathlib import Path

def calculate_score(directory: Path):
    total_score = 0

    for problem in range(1, 401):
        problem_file = Path(directory) / f"task{problem:03d}.py"
        if problem_file.exists():
            bytes_count = os.path.getsize(problem_file)
            score = max(1, 2500 - bytes_count)
            total_score += score

    return total_score

if __name__ == "__main__":
    directory = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    print(calculate_score(directory))

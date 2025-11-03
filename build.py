from pathlib import Path
import re
import sys
import compress


input_dir = Path("solutions")
output_dir = Path("build")


def main():
    if len(sys.argv) > 1:
        task_num = int(sys.argv[1])
        tasks = [task_num]
    else:
        tasks = range(1, 401)

    assert input_dir.exists(), f"{input_dir} does not exist"
    output_dir.mkdir(exist_ok=True)

    for i in tasks:
        filename = f"task{i:03d}.py"
        with open(input_dir / filename, "r", encoding="latin-1") as f:
            content = f.read()

        match = re.search(r"# compression: auto", content)

        content = content.split("\n#")[0]

        if match:
            source_bytes = content.encode("latin-1")
            compressed, _ = compress.compress(source_bytes)

            with open(output_dir / filename, "wb") as f:
                f.write(compressed)
        else:
            with open(output_dir / filename, "w", encoding="latin-1") as f:
                f.write(content)


if __name__ == "__main__":
    main()

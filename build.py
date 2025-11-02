from pathlib import Path
import re
import cgi_compression
import jailctf_compression
import generic_compression

def main():
    input_dir = Path("solutions")
    output_dir = Path("build")

    assert input_dir.exists(), f"{input_dir} does not exist"
    output_dir.mkdir(exist_ok=True)

    for i in range(1, 401):
        filename = f"task{i:03d}.py"
        with open(input_dir / filename, "r", encoding="latin-1") as f:
            content = f.read()

        compression_method = None
        compression_params = None

        match = re.search(r'# compression: (\w+)-(-?\d+)', content)
        if match:
            compression_method = 'specific'
            compression_params = (match.group(1), int(match.group(2)))
        else:
            match = re.search(r'# compression: (\w+)', content)
            if match:
                compression_method = match.group(1)

        content = content.split("\n#")[0]

        if compression_method:
            source_bytes = content.encode('latin-1')
            if compression_method == 'cgi' or compression_method == 'unknown':
                compressed = cgi_compression.compress(source_bytes)
            elif compression_method == 'jailctf':
                compressed = jailctf_compression.compress(source_bytes)
            elif compression_method == 'specific':
                method, window = compression_params
                compressed = generic_compression.compress(source_bytes, method, window)
            else:
                raise ValueError(f"Unknown compression method: {compression_method}")

            with open(output_dir / filename, "wb") as f:
                f.write(compressed)
        else:
            with open(output_dir / filename, "w", encoding="latin-1") as f:
                f.write(content)

if __name__ == "__main__":
    main()

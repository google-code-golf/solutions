tasks = [
    18,
    44,
    54,
    66,
    76,
    80,
    89,
    96,
    101,
    118,
    133,
    157,
    158,
    173,
    209,
    219,
    233,
    285,
    324,
    361,
    366,
]

for task in tasks:
    with open(f"build/task{task:03d}.py", "rb") as f:
        print(len(f.read()))

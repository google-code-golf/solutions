import zlib
import re
from zopfli.zlib import compress as zopfli_compress


def fix_backslashes(code_str: bytes):
    def update(m: re.Match[bytes]):
        data = m[0]
        if data[2] in b"\\'\"abfnNrtuUvox01234567879":
            return data
        return bytes((data[0], data[2]))

    return re.sub(br"\\\\.", update, code_str)


def make_code(compressed: bytes, add_wbits: bool, least_quote: int, most_quote: int):
    code_str = []
    for char in compressed:
        match char:
            case 0:
                code_str += [92, 48]
            case 0xa:
                code_str += [92, 110]
            case 0xd:
                code_str += [92, 114]
            case 0x27 | 0x22:
                if char == least_quote:
                    code_str += [92, least_quote]
                else:
                    code_str += [most_quote]
            case 0x5c:
                code_str += [92, 92]
            case _:
                code_str += [char]

    code_str = fix_backslashes(bytes(code_str))
    new_code = f"#coding:l1\nimport zlib\nexec(zlib.decompress(bytes({least_quote:c}".encode() + \
               code_str + \
               f"{least_quote:c},'l1'){',-9' if add_wbits else ''}))".encode()

    return new_code


def compress(code: str | bytes, max_brute: int = 10_000) -> bytes:
    code = code.strip()

    if isinstance(code, str):
        code = code.encode("utf-8")

    possible = [
        (zlib.compress(code), False),
        (zlib.compress(code, wbits=-15), True),
        *[(zopfli_compress(code, numiterations=iters or 15)[2:-4], True) for iters in range(0, max_brute, 1_000)]
    ]

    best = None
    for compressed, add_wbits in possible:
        least_quote = min(*b"'\"", key=compressed.count)
        most_quote = b"'\""[least_quote == b"'"[0]]

        cur_code = make_code(compressed, add_wbits, least_quote, most_quote)
        if best is None or len(cur_code) < len(best):
            best = cur_code

    assert best is not None

    return best

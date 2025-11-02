import zlib
import deflate
import zopfli.zlib

PREFIXES = [b"", b"\n", b"\r", b"\f", b"\n\f", b"\r\f"] + [
    bytes([c, ne]) for c in b"\t\n\f\r 0123456789#" for ne in b"\n\r"
]
POSTFIXES = [
    b"",
    b" ",
    b"\t",
    b"\n",
    b"\r",
    b"\f",
    b"#",
    b";",
    b"\t ",
    b" \t",
    b"\np",
] + [b"#" + bytes([n]) for n in range(32, 127)]


def compress_raw(src: bytes, method: str, window: int) -> tuple[bytes, dict]:
    header = b"#coding:L1\nimport zlib"
    if src[:9] == b"import re":
        header += b",re"
        src = src[10:]

    if method == "zopfli":
        iterations = window
        compressed = zopfli.zlib.compress(
            src, numiterations=iterations, blocksplitting=False
        )
        window = -(((compressed[0] >> 4) & 0x0F) + 8)
        compressed = compressed[2:-4]
    elif method == "libdeflate":
        compression_level = 12
        compressed = deflate.zlib_compress(src, compression_level)[2:-4]
    elif method == "zlib":
        compression_level = 9
        compressed = zlib.compress(src, compression_level, window)
    else:
        raise ValueError(f"Unknown method {method}")

    # Sanitize
    b_out = bytearray()
    for ch, ch1 in zip(compressed, compressed[1:] + b"'"):
        if ch == 0:
            b_out += b"\\x00" if ch1 in b"01234567" else b"\\0"
        elif ch == 13:
            b_out += b"\\r"
        elif ch == 92 and ch1 in b"\\\n\"'01234567NUabfnrtvxu":
            b_out += b"\\\\"
        else:
            b_out.append(ch)

    len_before_escape = len(compressed)
    compressed = bytes(b_out)

    # Choose delimiter
    delim = b'"""' if compressed[-1:] != b'"' else b"'''"
    newlines = compressed.count(ord("\n"))
    single = compressed.count(ord("'")) + newlines
    double = compressed.count(ord('"')) + newlines
    if 4 > single < double:
        delim = b"'"
        compressed = compressed.replace(b"'", b"\\'").replace(b"\n", b"\\n")
    elif 4 > double < single:
        delim = b'"'
        compressed = compressed.replace(b'"', b'\\"').replace(b"\n", b"\\n")

    stats = {
        "method": method,
        "window": window,
        "escape_cost": len(compressed) - len_before_escape,
    }

    if window < 15:
        window = -9

    if sum(c > 127 for c in compressed) < 8:
        header = header.replace(b"#coding:L1\n", b"")
        l = b""
        for c in compressed:
            l += b"\\x%0.2x" % c if c > 127 else bytes([c])
        compressed = l
        return header + b"\nexec(zlib.decompress(b" + delim + compressed + delim + (
            b",%d" % window if window < 15 else b""
        ) + b"))", stats

    return (
        header
        + b"\nexec(zlib.decompress(bytes("
        + delim
        + compressed
        + delim
        + b',"L1")'
        + (b",%d" % window if window < 15 else b"")
        + b"))",
        stats,
    )


def compress(source: bytes, method: str, window: int) -> bytes:
    best_zipped_src, best_stats = compress_raw(source, method, window)

    if len(best_zipped_src) > len(source) + 10:
        return source

    for pre in PREFIXES:
        for post in POSTFIXES:
            if len(pre + post) > 3:
                continue
            z_src, stats = compress_raw(pre + source + post, method, window)
            if len(z_src) < len(best_zipped_src):
                best_zipped_src, best_stats = z_src, stats

    return best_zipped_src

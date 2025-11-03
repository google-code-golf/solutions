import zlib

from reencode import reencode

import deflate
import zopfli.zlib


ZOPFLI_ITERS = [15, 128]
LIBDEFLATE_LEVELS = [11, 12]
ZLIB_LEVELS = [9]
DELIMS = [b"'", b'"']
WINDOWS = [-9, -10]


def sanitize(b_in: bytes, delim: bytes, use_reencode: bool = True) -> bytes:
    if use_reencode:
        b_in = reencode(b_in, delim)
    b_out = bytearray()
    for b, b_next in zip(b_in, [*b_in[1:], 0]):
        if b == 0:
            b_out += b"\\x00" if b_next in b"01234567" else b"\\0"
        elif b == ord("\r"):
            b_out += b"\\r"
        elif b == ord("\\") and b_next in b"\0\n\r\"'01234567NU\\abfnrtuvx":
            b_out += b"\\\\"
        elif b == ord("\n") and len(delim) == 1:
            b_out += b"\\n"
        elif bytes([b]) == delim:
            b_out += b"\\" + delim
        else:
            b_out.append(b)
    return bytes(b_out)


def compress(src: bytes) -> tuple[bytes, dict]:
    candidates: list[tuple[bytes, dict]] = []

    # import hoisting: "import zlib,re"
    hoisted_import = b""
    if src.startswith(b"import"):
        module = src.split()[1]
        hoisted_import = b"," + module
        src = src[len(module) + 8 :]

    compressed_data: list[tuple[bytes, str, int]] = []

    for iters in ZOPFLI_ITERS:
        full_result = zopfli.zlib.compress(
            src, numiterations=iters, blocksplitting=False
        )
        result = full_result[2:-4]
        actual_window = -(((full_result[0] >> 4) & 0x0F) + 8)

        compressed_data.append((result, f"zopfli(iters={iters})", -10))
        if actual_window != -10:
            output_window = -9 if actual_window < 15 else actual_window
            compressed_data.append((result, f"zopfli(iters={iters})", output_window))

    for level in LIBDEFLATE_LEVELS:
        result = bytes(deflate.deflate_compress(src, compresslevel=level))
        compressed_data.append((result, f"libdeflate(level={level})", -10))

    for level in ZLIB_LEVELS:
        for window in WINDOWS:
            if window == -10:
                result = zlib.compress(src, level=level, wbits=-15)[:]
            else:
                result = zlib.compress(src, level=level, wbits=window)[:]
            compressed_data.append((result, f"zlib(level={level})", window))

    for data, method, window in compressed_data:
        for delim in DELIMS:
            for use_reencode in [True, False]:
                sanitized = sanitize(data, delim, use_reencode=use_reencode)
                literal = delim + sanitized + delim

                window_str = (
                    b",~9"
                    if window == -10
                    else (b",%d" % window if window != 15 else b"")
                )

                code = (
                    b"#coding:L1\nimport zlib"
                    + hoisted_import
                    + b"\nexec(zlib.decompress(bytes("
                    + literal
                    + b',"L1")'
                    + window_str
                    + b"))"
                )

                candidates.append(
                    (
                        code,
                        {
                            "method": method,
                            "window": window,
                            "delimiter": delim.decode("latin-1"),
                            "reencode": use_reencode,
                        },
                    )
                )

    return min(candidates, key=lambda x: len(x[0]))

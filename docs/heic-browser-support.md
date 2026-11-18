# HEIC browser support and fallback workflow

HEIC is common in camera workflows but support varies by browser, operating system, codec availability, file brand, and embedded image features. A file extension alone does not guarantee successful decoding.

## Reliable workflow

1. Preserve the original HEIC file.
2. Attempt decoding in the current environment.
3. If decoding succeeds, check orientation, color, alpha, and HDR appearance.
4. Export JPEG for broad compatibility or PNG when transparency is required.
5. Compare the exported image before deleting any source.

Avoid claiming that every HEIC file can be decoded in every browser. A useful application should explain whether failure came from format detection, unsupported decoding, memory pressure, or a damaged file.

Try the [HEIC-compatible image converter](https://harnesstrail.com/en/convert-image/).

# Browser Media Tools and Format Guide

Open reference data, runnable browser examples, and privacy-first tools for working with images, video, and documents.

[![Website](https://img.shields.io/badge/website-HarnessTrail-0000ff)](https://harnesstrail.com/)
[![License: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE)
[![Data: CC0](https://img.shields.io/badge/data-CC0-green.svg)](DATA-LICENSE)

## Why this repository exists

Choosing an image format or processing workflow often requires scattered compatibility tables, vague quality claims, and server-side upload services. This repository keeps the practical parts in one place:

- machine-readable format capability data;
- feature-detection recipes that test the current browser instead of guessing from a browser name;
- small, dependency-free examples for compression, WebP conversion, metadata-safe re-encoding, and video frame extraction;
- a reproducible benchmark method and an empty results template;
- links to free local browser tools when a complete interface is more useful than a code sample.

## Try the online tools

HarnessTrail processes supported files locally in the browser. Source files do not need to be uploaded to a processing server.

| Task | Online tool |
| --- | --- |
| Compress images | [Image compressor](https://harnesstrail.com/en/compress-image/) |
| Convert JPG, PNG, WebP, AVIF, HEIC, or TIFF | [Image converter](https://harnesstrail.com/en/convert-image/) |
| Resize images | [Image resizer](https://harnesstrail.com/en/resize-image/) |
| Convert video to GIF | [Video to GIF](https://harnesstrail.com/en/video-to-gif/) |
| Combine images into PDF | [Images to PDF](https://harnesstrail.com/en/images-to-pdf/) |
| Remove EXIF metadata | [Metadata remover](https://harnesstrail.com/en/remove-exif/) |

## Repository contents

### Data

- [`format-capabilities.csv`](data/format-capabilities.csv) — transparency, animation, lossless, HDR, and common-use characteristics.
- [`format-capabilities.json`](data/format-capabilities.json) — the same records as structured JSON.
- [`browser-feature-tests.json`](data/browser-feature-tests.json) — recommended runtime tests for decoding and encoding.
- [`benchmark-template.csv`](data/benchmark-template.csv) — a neutral schema for publishing reproducible results.

### Runnable examples

Download or clone the repository and open any file in `examples/` in a modern browser:

- [`detect-image-support.html`](examples/detect-image-support.html)
- [`convert-image-to-webp.html`](examples/convert-image-to-webp.html)
- [`compress-image.html`](examples/compress-image.html)
- [`metadata-safe-reencode.html`](examples/metadata-safe-reencode.html)
- [`extract-video-frame.html`](examples/extract-video-frame.html)

Examples intentionally use browser APIs without a framework, build step, analytics, or network request.

### Guides

- [JPG vs PNG vs WebP vs AVIF](docs/jpg-png-webp-avif.md)
- [Compression quality and dimensions](docs/compression-quality-and-dimensions.md)
- [HEIC support and fallback workflow](docs/heic-browser-support.md)
- [How local browser processing works](docs/local-browser-processing.md)
- [Reproducible benchmark methodology](docs/benchmark-methodology.md)

## Quick start

```bash
git clone https://github.com/HarnessTrail/browser-media-tools.git
cd browser-media-tools
python3 -m http.server 8080
```

Then open `http://localhost:8080/examples/detect-image-support.html`.

A local server is recommended because browser security rules can restrict some APIs on `file://` pages.

## Data notes

Format capabilities describe the formats themselves. Browser implementation support changes over time, so the examples use runtime feature detection. Do not treat a static browser-version table as a permanent guarantee.

Benchmark result rows are deliberately not prefilled with invented figures. Follow the documented method, retain the source fixtures, and include environment details with every published result.

## Contributing

Corrections, additional fixtures, accessibility improvements, and reproducible benchmark results are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## Licenses

- Code and examples: [MIT](LICENSE)
- Data and documentation: [CC0 1.0](DATA-LICENSE)

Maintained by [HarnessTrail](https://harnesstrail.com/) · [support@harnesstrail.com](mailto:support@harnesstrail.com)

# Reproducible image benchmark methodology

A useful benchmark publishes enough information for another person to repeat it.

## Fixture set

Use licensed fixtures from at least four classes: photograph, screenshot, flat illustration, and transparent graphic. Retain original files and publish SHA-256 checksums.

## Controls

- Record operating system, browser, encoder, and versions.
- Run one warm-up and at least five measured encodes.
- Keep source dimensions constant for format comparison.
- Report resize operations separately.
- Use the same color-management policy.
- Report quality settings without assuming equal numbers mean equal visual quality.

## Measurements

Record elapsed time, output bytes, dimensions, alpha preservation, and visual-quality metrics when appropriate. Automated metrics do not replace visual inspection. Report median timing and describe outliers.

## Publication

Use `data/benchmark-template.csv`. Do not omit failed runs. Explain unsupported formats, memory failures, or decoder errors instead of silently removing them.

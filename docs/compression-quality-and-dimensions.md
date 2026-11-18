# Compression quality and dimensions

Image byte size is shaped by pixel dimensions, content complexity, format, encoder, quality, metadata, and color representation. Reducing quality alone is not always the best first step.

## Recommended order

1. Crop unused regions.
2. Resize to the largest size actually displayed.
3. Select a format suited to the content.
4. Adjust quality while inspecting the intended display size.
5. Remove unneeded metadata from a copy.
6. Verify dimensions, bytes, alpha, color, and visible artifacts.

A 4000 × 3000 image contains twelve million pixels even when the compressed file looks small. Decoding can therefore consume much more memory than the file size suggests. Process very large images in smaller batches, especially on mobile devices.

For a complete interface, use [compress to a target size](https://harnesstrail.com/en/compress-to-size/).

# How local browser processing works

A local browser tool reads a user-selected file through browser APIs, decodes it in memory, transforms it with canvas, WebCodecs, WebAssembly, or JavaScript, and creates a new Blob for download.

## Privacy boundary

Local processing can keep source bytes on the device, but that statement should be verified for each product. Network analytics, external error reporting, fonts, and other resources are separate from the file-processing path. Browser developer tools can be used to inspect network activity during a test.

## Operational limits

- Decoded images may use many times the compressed file size in memory.
- Video processing is constrained by duration, frame rate, dimensions, and codec support.
- Mobile browsers can terminate memory-intensive tabs.
- Output encoding support differs by browser.
- Closing or refreshing the page usually discards in-memory results.

HarnessTrail documents its local-processing behavior on its [privacy page](https://harnesstrail.com/en/privacy/).

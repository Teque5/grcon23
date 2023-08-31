# Noir 2: The Allure of Secrets (Falcon STL)

## Solution

* 37 points
* Topic: 3D Printing / QR Code
* `flag{6175422652}`

## Explanation

QR code is hidden with the STL file. Can be seen by loading into any 3d modeling software, but was intended to be found by using a 3d printing slicer.

## Generate

### Getting started

1) Original [Maltese Falcon](https://www.thingiverse.com/thing:46631/files) STL.
2) Create QR code SVG:
    `qrencode -l L -t SVG -o /media/ring/Unorganized/falcon.svg "Picking up an elegant scarf, Vivian noticed an unexpected detail—an ornate design that concealed a telephone number: 6175422652" -m 2 -d 8 -s 1`
3) Combined within blender and exported.

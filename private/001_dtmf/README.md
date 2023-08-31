# Noir 2: The Allure of Secrets (DTMF)

## Solution

* 41 points
* Topic: DSP / Voice Grade Channel / Phreaking
* `flag{elegant}`

## Explanation

This is a puzzle where one is meant to recognize the dual tone multi frequency encoding of a sequence of numbers representing a message string. The message is encoded as a sequence of numbers using a [multi-tap cipher](https://en.wikipedia.org/wiki/Multi-tap) reminiscent of the olden days of mobile phone text entry.

## Generating the wav file

run `python3 generate_wav.py`
### Dependencies

* numpy
* scipy

# Noir 3: Unscrambling the Echos

## Solution

* 71 points
* Topic: GNU Radio Companion / DSP / SigMF
* `flag{coiffure}`

## General Idea

Great flowgraph for voice scrambler and provide a sample input and output. Embed the flag in the voice recording.

I really like the way [the CRY2001 scrambler](https://www.sigidwiki.com/wiki/CRY2001_Voice_Scrambler) sounds and I'd like to create a flowgraph for encoding / decoding.

Use the [Black mesa announcement system](https://tz-dev.github.io/hl_text2speech/index.html#) for generating clue. It supports most of the NATO alphabet: alpha bravo  charlie delta echo foxtrot gordon hotel india juliet kilo lima mike november oscar portal quebec romeo sierra tango uniform victor whiskey xeno yankee zulu

## Encoded phrase

1) "Vivian, this is your pathfinder in the night. Follow my lead to the realm of forgotten metal and rust. The junkyard's symphony holds the notes of a tale waiting to be deciphered. Amidst the discarded fragments, truths unfurl like blooms in the moonlight. Let the winds of fate guide you, and you shall find what you seek."

2) woop acknowledge message boop charlie oscar india foxtrot foxtrot uniform romeo echo acknowledged boop

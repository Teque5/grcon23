# # Noir 0: The Enigmatic Invitation (Magic Eye)

## Solution

* 23 points
* Topic: Stegonography / Magic Eye / Image Filtering
* `flag{squirrel}`

## Explanation

This is a stereogram that requires image filtering first in order to view the final squirrel image clearly. Python code is used to reduce blur noise, and then [a magic eye solver program](https://magiceye.ecksdee.co.uk/) is used to solve the stereogram. 

Visual inspection, additional Python code, or Photoshop could also be useful for seeing the squirrel/solving the stereogram (untested).

## Generating the image

### Getting started
1. Use the best filter to reduce blur noise. 
2. Then, the stereogram should be clear enough to see/solve the image.

### Dependencies
* python, opencv, pyplot

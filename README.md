# noiseTest
**Summary**

A little noise generation tool that i made during an English class, make surprisingly stunning rock texture maps and can be layered on top of eachother for exotic results.

**Requirements**

Python 3.8.2 is the earliest version the script has been tested to work on, might work with older versions.
*Pillow* for Python, more info at: [Pillow Installation Page](https://pillow.readthedocs.io/en/stable/installation.html "Installation Page")

**Use**

Basically what the program does is it takes 3 input parameters that are all **integers**:
`resolution` represents the length and width of the final image,
`density` a parameter from which the program randomizes out white dots onto a black image, the higher the value the sparser and fewer the "noise cells" will be,
`intensity` the times the program loops through the image and smudges the white spots, the higher the value the darker and more smudged the final image will look.
Some parameters have a more drastic impact than others, play around with them to see what yields the best result for you!

**Functionality**

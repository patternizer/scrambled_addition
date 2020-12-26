![image](https://github.com/patternizer/scrambled_addition/blob/master/scrambled_addition_puzzle.JPG)

# Scrambled Addition

Python code to generate scrambled addition puzzles with scrambled solutions inspired by the 'srcmalbed nmebur plzuze' posted by Alex Bellos at the Guardian: https://www.theguardian.com/science/2020/nov/16/can-you-solve-it-the-srcmalbed-nmebur-plzuze.

You can use this code to generate your own puzzles for numbers of any length and number of numbers. Enjoy!

## Contents

* `scrambled_addition.py` - main script for generating puzzle variants
* `scrambled_addition_puzzle.JPG` - solution approach for Alex's posted puzzle

The first step is to clone the latest scrambled_addition code and step into the check out directory:

    $ git clone https://github.com/patternizer/scrambled_addition.git
    $ cd scrambled_addition

### Using Standard Python

The code should run with the [standard CPython](https://www.python.org/downloads/) installation and was tested in a conda virtual environment running a 64-bit version of Python 3.8.

For puzzles of other length and number edit the lines:

intlength = 5 # number of digits per number
intnumber = 3 # number of numbers to add

and run with:

    $ python scrambled_addition.py

## License

My code for the app is distributed under terms and conditions of the [Unlicense](https://unlicense.org/).

## Contact information

* [Michael Taylor](https://patternizer.github.io)



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

#------------------------------------------------------------------------------
# PROGRAM: scrambled_adds.py
#------------------------------------------------------------------------------
# Version 0.1
# 16 November, 2020
# Michael Taylor
# https://patternizer.github.io
# https://people.uea.ac.uk/michael_a_taylor
# michael.a.taylor@uea.ac.uk

#------------------------------------------------------------------------------

"""

import numpy as np

intlength = 5 # number of digits per number
intnumber = 3 # number of numbers to add

def scrambled_add(intlength,intnumber):

    numbers = np.random.random_integers(low=10**(intlength-1), high=10**(intlength)-1, size=intnumber)
    numbers_total = np.sum(numbers)
    addition = np.append(numbers, numbers_total)
    scrambled = []
    for j in range(len(addition)):
        numberstr = str(addition[j])[0]
        middlestr = str(addition[j])[1:-1]
        while (middlestr == str(addition[j])[1:-1]):
            middle = np.random.permutation([str(addition[j])[1+i] for i in range(len(str(addition[j])[1:-1])) ])
            middlestr = ""
            for i in range(len(middle)):
                middlestr = middlestr + str(middle[i])
        numberstr = numberstr + middlestr
        numberstr = numberstr + str(addition[j])[-1]
        scrambled = np.append(scrambled, int(numberstr))        
    scrambled_numbers = scrambled[0:-1].astype(int)
    scrambled_numbers_total = scrambled[-1].astype(int)
    return numbers, numbers_total, scrambled_numbers, scrambled_numbers_total    

numbers, numbers_total, scrambled_numbers, scrambled_numbers_total = scrambled_add(intlength,intnumber)

print('numbers to be added:', numbers)
print('total = ', numbers_total)
print('scrambled numbers to be added:', scrambled_numbers)
print('scrambled total = ', scrambled_numbers_total)

#------------------------------------------------------------------------------
print('** END')        



"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""

import random
import sys

def RandomStringGenerator(l=12, a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']):
    p = 0
    s = ''
    while p<l:
        s += random.choice(a)
        p += 1
    return s

def BatchStringGenerator(n, a=8, b=12):
    r = []
    for i in range(n):
        c = None
        if a < b:
            c = random.choice(range(a, b))
        elif a == b:
            c = a
        else:
            sys.exit('Incorrect min and max string lengths. Try again.')
        r.append(RandomStringGenerator(c))
    return r

try:
    a = int(input('Enter minimum string length: '))
    b = int(input('Enter maximum string length: '))
    n = int(input('How many random strings to generate? '))
except ValueError:
    print("Incorrect input, this program only accepts digits as user defined input.")

print(BatchStringGenerator(int(n), int(a), int(b)))
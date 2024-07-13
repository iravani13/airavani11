#!/usr/bin/env python3

import sys


if len(sys.argv) == 2:
     
    print("Incorrect number of arguments provided.")
    sys.exit(1)


name = sys.argv[1]
age = sys.argv[2]


age = int(age)


print('Hi ' + name + ', you are ' + str(age) + ' years old.')


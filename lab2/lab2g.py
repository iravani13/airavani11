#!/usr/bin/env python3
# Author: Amir Iravani
# Author ID: airavani1
# Date Created: 2024/06/04

import sys

# Check the number of arguments
if len(sys.argv) == 1:
    timer = 3  # Assign the value 3 to timer when no arguments are provided
elif len(sys.argv) == 2:
    timer = int(sys.argv[1])  # Assign the value of the first argument to timer if it's a valid integer
else:
    print ("Error: This script requires at most one argument. Please provide a single integer value.")
    sys.exit(1)  # Exit with a non-zero error code to indicate failure

# WHILE loop that repeats until timer equals 0
while timer > 0:
    print (timer)
    timer = timer -1  # Decrement the timer by 1

print("blast off!")









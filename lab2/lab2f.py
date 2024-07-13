#!/usr/bin/env python3
# Author: Amir Iravani
# Author ID: airavani1
# Date Created: 2024/06/04

import sys

if len(sys.argv) != 2:
    print("Error")
    sys.exit(1)  # Exit with a non-zero error code to indicate failure

timer = int(sys.argv[1])  # Use the first command-line argument

while timer > 0:
    print(timer)
    timer = timer - 1

print("blast off!")








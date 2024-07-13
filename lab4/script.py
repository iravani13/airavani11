#!/usr/bin/env python3
#Mohammad Mehdi Hassan - mhassan99 - OPS445NCC - Quiz 3

import sys

def read_file(filename: str) -> list:
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return ['File not found!']

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: no file specified.")
    else:
        filename = sys.argv[1]
        contents = read_file(filename)
        for line in contents:
            print(line, end='')
        print("\nNumber of lines:", len(contents))

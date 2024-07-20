#!/usr/bin/env python3
# Author ID: airavani1

def add(number1, number2):
    try:
        result = int(number1) + int(number2)
        return result
    except Exception as e:
        return 'error: could not add numbers'

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return lines
    except Exception as e:
        return 'error: could not read file'

# Sample Run 2 (with import)
if __name__ == '__main__':
    print(add(10, 5))                     # Sample Run 2
    print(add('10', 5))                   # Sample Run 2
    print(add('10', '5'))                 # Sample Run 2
    print(add('abc', '5'))                # Sample Run 2
    print(add('hello', 'world'))          # Sample Run 2
    print(read_file('seneca2.txt'))       # Sample Run 2
    print(read_file('file10000.txt'))     # Sample Run 2

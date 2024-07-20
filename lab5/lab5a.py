#!/usr/bin/env python3
# Author ID: airavani1

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return 'File not found!'

def read_file_list(file_name):
    # Takes a file_name as string for a file name,
    # return its entire contents as a list of lines without new-line characters
    try:
        with open(file_name, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return ['File not found!']

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))

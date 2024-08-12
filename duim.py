
#!/usr/bin/env python3
import subprocess
import sys
import argparse

"""
OPS445 Assignment 2
Program: duim.py
Author: Amir Iravani
The python code in this file (duim.py) is original work written by
"Amir Iravani". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or online resource. I have not shared this python script
with anyone or anything except for submission for grading.
I understand that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
Description: <Enter your documentation here>
Date: 2024-08-11
"""

def parse_command_args():
    """Set up and return command-line arguments."""
    parser = argparse.ArgumentParser(description="DU Improved -- Disk Usage Report with bar charts", epilog="Copyright 2023")
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify graph length. Default is 20.")
    parser.add_argument("-H", "--human-readable", action="store_true", help="Show sizes in human-readable format (e.g., 1K 234M 2G)")
    parser.add_argument("target", nargs=1, help="Target directory to analyze")
    return parser.parse_args()

def percent_to_graph(percent: int, total_chars: int) -> str:
    """Convert a percentage to a graph bar."""
    num_symbols = round((percent / 100) * total_chars)
    return '#' * num_symbols + ' ' * (total_chars - num_symbols)

def call_du_sub(location: str) -> list:
    """Run 'du' on a directory and return the output as a list."""
    result = subprocess.run(['du', '-d', '1', location], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip().split('\n')

def create_dir_dict(raw_dat: list) -> dict:
    """Convert raw 'du' output into a dictionary of sizes."""
    dir_dict = {}
    for line in raw_dat:
        size, path = line.split('\t')
        dir_dict[path] = int(size)
    return dir_dict

def bytes_to_human_r(kibibytes: int, decimal_places: int=2) -> str:
    """Convert a size in KiB to a human-readable format."""
    suffixes = ['KiB', 'MiB', 'GiB', 'TiB', 'PiB']
    suf_count = 0
    result = kibibytes
    while result >= 1024 and suf_count < len(suffixes) - 1:
        result /= 1024
        suf_count += 1
    return f'{result:.{decimal_places}f} {suffixes[suf_count]}'

if __name__ == "__main__":
    args = parse_command_args()
    raw_data = call_du_sub(args.target[0])
    dir_dict = create_dir_dict(raw_data)
    max_size = max(dir_dict.values())

    for directory, size in dir_dict.items():
        percent = (size / max_size) * 100
        graph = percent_to_graph(percent, args.length)
        size_str = bytes_to_human_r(size) if args.human_readable else f'{size}K'
        print(f'{size_str}\t{graph}\t{directory}')

#!/usr/bin/env python3

'''
OPS445 Assignment 2
Program: assignment2.py 
Author: Amir Iravani
Semester: Summer 2024

The python code in this file is original work written by
Amir Iravani. No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or online resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: This Python script visualizes memory usage on a Linux system.
It provides two main functionalities:
1. Display the total memory usage of the system if no specific program is mentioned.
2. Display memory usage statistics of processes associated with a specified program.
'''

import argparse
import os
import sys

def parse_command_args() -> object:
    """
    Set up and parse command-line arguments for the script.

    Returns:
        argparse.Namespace: Parsed command-line arguments, including options for graph length,
        human-readable format, and optional program name.
    """
    parser = argparse.ArgumentParser(
        description="Memory Visualizer -- Displays Memory Usage Report with bar charts",
        epilog="Copyright 2023"
    )
    
    parser.add_argument(
        "-l", "--length",
        type=int,
        default=20,
        help="Set the length of the graph. Default length is 20 characters."
    )
    
    parser.add_argument(
        "-H", "--human-readable",
        action="store_true",
        help="Display memory sizes in a human-readable format (e.g., MiB, GiB)."
    )
    
    parser.add_argument(
        "program",
        type=str,
        nargs='?',
        help="Specify the name of a program to display memory usage for its processes. "
             "If omitted, displays total system memory usage."
    )
    
    return parser.parse_args()

def percent_to_graph(percent: float, length: int = 20) -> str:
    """
    Convert a memory usage percentage to a textual bar graph representation.

    Args:
        percent (float): Memory usage percentage, between 0.0 and 1.0.
        length (int): The total length of the graph in characters.

    Returns:
        str: A string representing the bar graph, with '#' characters for used memory
             and spaces for unused memory.
    """
    percent = max(0.0, min(1.0, percent))  # Ensure percent is within the range [0.0, 1.0]
    num_symbols = round(percent * length)   # Calculate the number of '#' symbols to represent the usage
    return '#' * num_symbols + ' ' * (length - num_symbols)  # Create the bar graph string

def get_sys_mem() -> int:
    """
    Retrieve the total system memory from the /proc/meminfo file.

    Returns:
        int: Total system memory in kilobytes (kB).
    """
    with open('/proc/meminfo', 'r') as f:
        total_line = next(line for line in f if line.startswith('MemTotal'))
        total_memory = int(total_line.split()[1])
    return total_memory

def get_avail_mem() -> int:
    """
    Retrieve the available system memory from the /proc/meminfo file.

    Returns:
        int: Available system memory in kilobytes (kB).
    """
    with open('/proc/meminfo', 'r') as f:
        avail_line = next(line for line in f if line.startswith('MemAvailable'))
        avail_memory = int(avail_line.split()[1])
    return avail_memory

def pids_of_prog(app_name: str) -> list:
    """
    Obtain a list of process IDs (PIDs) for the given application.

    Args:
        app_name (str): The name of the application to find PIDs for.

    Returns:
        list: A list of PIDs associated with the specified application.
    """
    pid_list = []
    try:
        pidof_output = os.popen(f"pidof {app_name}").read().strip()  # Get the list of PIDs from `pidof`
        pid_list = pidof_output.split()  # Split the output into a list of PIDs
    except Exception as e:
        print(f"Error: {e}")  # Print error message if `pidof` fails
    return pid_list

def rss_mem_of_pid(proc_id: str) -> int:
    """
    Retrieve the resident set size (RSS) memory of a process with a given PID.

    Args:
        proc_id (str): The process ID to query.

    Returns:
        int: Resident memory usage of the process in kilobytes (kB). Returns 0 if the process or 
             its memory information is not found.
    """
    try:
        with open(os.path.join('/proc', str(proc_id), 'status'), 'r') as status_file:
            for line in status_file:
                if line.startswith('VmRSS'):
                    rss_memory = int(line.split()[1])  # Extract the RSS value from the file
                    return rss_memory
    except FileNotFoundError:
        pass  # If the file or process is not found, return 0
    return 0

def bytes_to_human_r(kibibytes: int, decimal_places: int = 2) -> str:
    """
    Convert a memory size in kibibytes to a more human-readable format (e.g., KiB to GiB).

    Args:
        kibibytes (int): Size in kibibytes.
        decimal_places (int): Number of decimal places to include in the output.

    Returns:
        str: Memory size formatted in a human-readable unit (KiB, MiB, GiB, etc.).
    """
    suffixes = ['KiB', 'MiB', 'GiB', 'TiB', 'PiB']  # Units for converting memory size
    suf_count = 0
    result = kibibytes
    
    while result > 1024 and suf_count < len(suffixes) - 1:
        result /= 1024  # Convert to the next unit
        suf_count += 1
    
    return f'{result:.{decimal_places}f} {suffixes[suf_count]}'  # Format the result with the appropriate unit

if __name__ == "__main__":
    args = parse_command_args()
    
    if not args.program:
        # No specific program provided; display system memory usage
        total_memory = get_sys_mem()
        used_memory = total_memory - get_avail_mem()  # Calculate used memory
        percent_used = used_memory / total_memory  # Calculate the percentage of used memory
        graph = percent_to_graph(percent_used, args.length)  # Create the bar graph for memory usage
        
        if args.human_readable:
            # Display memory usage in human-readable format
            print(f"Memory         [{graph} | {percent_used * 100:.0f}%] {bytes_to_human_r(used_memory)}/{bytes_to_human_r(total_memory)}")
        else:
            # Display memory usage in kilobytes
            print(f"Memory         [{graph} | {percent_used * 100:.0f}%] {used_memory}/{total_memory} kB")
    else:
        # Program specified; display memory usage for processes related to that program
        pid_list = pids_of_prog(args.program)
        
        if not pid_list:
            print(f"{args.program} not found.")  # Inform the user if the program has no running processes
            sys.exit(1)
        
        total_used_memory = 0
        total_memory = get_sys_mem()

        for pid in pid_list:
            rss_memory = rss_mem_of_pid(pid)  # Get RSS memory usage for each PID
            total_used_memory += rss_memory  # Accumulate total used memory
            percent_used = rss_memory / total_memory  # Calculate the percentage of memory used by this process
            graph = percent_to_graph(percent_used, args.length)  # Create the bar graph for each PID
            
            if args.human_readable:
                # Display each PID's memory usage in human-readable format
                print(f"{pid:<16}[{graph} | {percent_used * 100:.0f}%] {bytes_to_human_r(rss_memory)}/{bytes_to_human_r(total_memory)}")
            else:
                # Display each PID's memory usage in kilobytes
                print(f"{pid:<16}[{graph} | {percent_used * 100:.0f}%] {rss_memory}/{total_memory} kB")
        
        # Display total memory usage for the specified program
        percent_used = total_used_memory / total_memory
        graph = percent_to_graph(percent_used, args.length)
        
        if args.human_readable:
            print(f"{args.program:<16}[{graph} | {percent_used * 100:.0f}%] {bytes_to_human_r(total_used_memory)}/{bytes_to_human_r(total_memory)}")
        else:
            print(f"{args.program:<16}[{graph} | {percent_used * 100:.0f}%] {total_used_memory}/{total_memory} kB")

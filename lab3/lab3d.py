#!/usr/bin/env python3
# Author ID: airavani1

import subprocess

def free_space():
    # Launch the command and get the output
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", shell=True, stdout=subprocess.PIPE)
    output = p.communicate()
    
    # Decode the bytes output and strip off newline characters
    stdout = output[0].decode('utf-8').strip()
    return stdout

if __name__ == '__main__':
    print(free_space())

#!/usr/bin/env python3
# Student ID: airavani1

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def change_time(time, seconds):
    # Add the seconds to the time's seconds attribute
    time.second += seconds
    
    # Handle carry over for seconds
    while time.second >= 60:
        time.second -= 60
        time.minute += 1

    while time.second < 0:
        time.second += 60
        time.minute -= 1

    # Handle carry over for minutes
    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1

    while time.minute < 0:
        time.minute += 60
        time.hour -= 1

    # Handle negative hour
    while time.hour < 0:
        time.hour += 24

# Testing the changes in the interactive shell
if __name__ == "__main__":
    time1 = Time(9, 50, 0)
    print(format_time(time1))  # Should print 09:50:00
    seconds = 1800
    change_time(time1, seconds)
    print(format_time(time1))  # Should print 10:20:00
    seconds = -1800
    change_time(time1, seconds)
    print(format_time(time1))  # Should print 09:50:00


class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    sum = Time(0, 0, 0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    # Carry over seconds to minutes
    if sum.second >= 60:
        sum.minute += sum.second // 60
        sum.second = sum.second % 60

    # Carry over minutes to hours
    if sum.minute >= 60:
        sum.hour += sum.minute // 60
        sum.minute = sum.minute % 60

    return sum

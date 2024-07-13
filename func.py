#!/usr/bin/env python3

def items_after_four(iterable):
    """
    If the length of a list is less than or equal to four, return zero. Otherwise, return the length minus four.
    """
    # Slice the list  
    sliced_list = iterable[4:]
    
    # The length of the sliced list gives the number of elements after the fourth
    return len(sliced_list)

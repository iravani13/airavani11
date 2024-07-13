#!/usr/bin/env python3

def vowel_counter(target_string):
    """Does a thing, counts stuff, doesn't work, fix later : P"""

    vowel_tally = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    for char in target_string.lower():
        if char in vowel_tally.keys():0
            vowel_tally[char] +=1 

    return vowel_tally

if __name__ == "__main__":
    test_string = "It was the best of times, it was the blurst of times."
    results = vowel_counter(test_string)
    print(results)

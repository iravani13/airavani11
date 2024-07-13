#!/usr/bin/env python3

"""
Author: amir  iravani
This script prompts the user for numbers until an empty string is entered,
then calculates and returns the average of those numbers.
"""

def main():
    numbers = []
    
    while True:
        user_input = input("Enter a number : ")
        
        if user_input == "":
            break
        
        if user_input.isnumeric():
            numbers.append(int(user_input))
    
    if numbers:
        average = sum(numbers) / len(numbers)
        print("The average is {}".format(average))
    else:
        print("No valid numbers were entered.")

if __name__ == "__main__":
    main()


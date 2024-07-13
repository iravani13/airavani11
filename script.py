#!/usr/bin/env python3
"""
script.py
A script to interact with the user about their preferences for cafeteria food.
"""

# Creating an immutable iterable with at least four items
cafeteria_food = ('pizza', 'burger', 'salad', 'pasta')

# For each item in cafeteria_food, ask the user if they like it or not
for food in cafeteria_food:
    response = input("Do you like " + food + "? ")

# If we wanted to save the user's response to each prompt and associate the response with the food in question, we would use a dictionary.
# Example:
# user_responses = {'pizza': 'yes', 'burger': 'no', 'salad': 'yes', 'pasta': 'no'}


__author__ = 'jc455953'
"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        result=int(input("enter a number:"))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
else:
 print("Valid result is:", result)
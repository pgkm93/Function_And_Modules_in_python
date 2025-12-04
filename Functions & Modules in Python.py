## Assignment 3
#Functions & Modules in Python

#Task 1
# Calculation factorial using a function

import math

#takeing input from user
a = int(input("Enter the number:"))

#printing result using f" "string function
print(f"The factorial of {a} is {math.factorial(a)}")


# Task 2
# Math module for calculation
try:
    b = input("Enter a number:")
    c = float(b)
except ValueError:
    print("Please enter the ,Invalid input")

#2.
#a.o square root of the number
if 0 <= c:
    square_root = math.sqrt(c)
else:
    square_root = "Cannot calculate square root of a negative number"

#b o Natural logarithm of the number
if c >= 0:
    natural_log = math.log(c)
else:
    natural_log = "Cannot calculate natural log"

#o sine of the number
sine_value = math.sin(c)

#3.results
print(f" Square root:{square_root}")
print(f"Natural logarithm :{natural_log}")
print(f"Sine value:{sine_value}")











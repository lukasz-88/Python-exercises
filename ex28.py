"""
Exercise 28: Max Of Three
Implement a function that takes as input three variables, and returns the
largest of the three. Do this without using the Python max() function!
The goal of this exercise is to think about some internals that Python
normally takes care of for us. All you need is some variables and
if statements!
"""


def max_three(var1, var2, var3):
    if int(var1) > int(var2) and int(var1) > var3:
        return var1
    elif int(var2) > int(var3):
        return var2
    else:
        return var3


print(max_three(2, 5, 1))
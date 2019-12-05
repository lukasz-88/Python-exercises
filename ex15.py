"""
Exercise 15: Reverse Word Order
Write a program (using functions!) that asks the user for a long string
containing multiple words. Print back to the user the same string,
except with the words in backwards order. For example, say
I type the string: My name is Michele
Then I would see the string:  Michele is name My
shown back to me.
"""

def string_backward(user_string: str):
    if len(user_string) == 0:
        print("Zero-length string")
    else:
        print(" ".join(user_string.split(" ")[::-1]))

string_backward("My name is Michele")

"""
Exercise 12: List Ends
Write a program that takes a list of numbers
(for example, a = [5, 10, 15, 20, 25]) and makes a new list of
only the first and last elements of the given list. For practice,
write this code inside a function.
"""

a = [5, 10, 15, 20, 25]


def list_ends(user_list):
    print([user_list[0], user_list[-1]])


list_ends(a)

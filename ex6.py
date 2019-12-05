"""
Exercise 6: String Lists
Ask the user for a string and print out whether this
string is a palindrome or not. (A palindrome is a string
that reads the same forwards and backwards.)
"""

user_str = list(input("Enter some string: "))

if user_str[:] == user_str[::-1]:
    print("Word is palindrome")
else:
    print("Word is not palindrome")


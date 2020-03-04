"""
Exercise 1: Character Input
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them
the year that they will turn 100 years old.

Extras:
1.Add on to the previous program by asking the user for another number
and printing out that many copies of the previous message.
(Hint: order of operations exists in Python)
2.Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button)
"""

from datetime import datetime

while True:
    name = input("What's your name: ")
    if name.isalpha() == False:
        print("Incorrect input. Try again.")
        continue
    else:
        break

print("Your name is " + name)

while True:
    age = input("Enter your age: ")
    if age.isdigit() == False:
        print("Incorrect input. Try again.")
        continue
    else:
        break

while True:
    number_copy = input("How many copies print? ")
    if not number_copy.isdigit() or int(number_copy) <= 0:
        print("Number of copies must be a positive number")
        continue
    else:
        break

current_year = datetime.now().year
year100 = current_year + (100 - int(age))

msg = 'Your age is: {}. You will be 100 years old in: {}\n'.format(age,year100)
print(msg * int(number_copy))

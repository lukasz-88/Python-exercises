"""
Exercise 2: Odd Or Even
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:
1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and
one number to divide by (check). If check divides evenly into num, tell
that to the user. If not, print a different appropriate message.
"""



""" VERSION_1:
    
while True:
    try:
        user_num = int(input("Enter integer number: "))
    except ValueError:
        print("Incorrect input. Try again.")
        continue
    else:
        break

if user_num % 2 == 0:
    if user_num % 4 == 0:
        print("Your number is even and is divisible by 4")
    else:
        print("Your number is even")
else:
    print("Your number is odd")
"""


#VERSION_2
while True:
    try:
        user_num = int(input("Enter integer number: "))
    except ValueError:
        print("Incorrect input. Try again.")
        continue
    else:
        break

while True:
    try:
        user_num2 = int(input("Enter the number to divide by: "))
    except ValueError:
        print("Incorrect input. Try again.")
        continue
    else:
        break

if user_num % user_num2 == 0:
    print("Your number is divisible by the second number")
else:
    print("Your number isn't divisible by the second number")

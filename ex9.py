"""
Exercise 9: Guessing Game One
Generate a random number between 1 and 9 (including 1 and 9). Ask the user
to guess the number, then tell them whether they guessed too low, too high,
or exactly right. (Hint: remember to use the user input lessons from
the very first exercise)

Extras:
1) Keep the game going until the user types “exit”
2) Keep track of how many guesses the user has taken, and when
the game ends, print this out.
"""

import random

number = random.randint(1,9)
counter = 0

while True:
    try:
        user_number = int(input("Try to guess the number between 1 and 9: "))
        if user_number in range(1,10):
            counter += 1
            if user_number == number:
                print("Correct! You tried to guess {} time(s)".format(counter))
            elif user_number < number:
                print("Your number is lower")
                continue
            else:
                print("Your number is greater")
                continue
        else:
            print("Incorrect number")
            continue
    except ValueError:
        print("Incorrect value")
        continue
    
    check = input("One more game? If not, please type 'quit': ")
    if check == 'quit':
        break
    else:
        counter = 0
        continue

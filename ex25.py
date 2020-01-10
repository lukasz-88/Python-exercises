"""
Exercise 25: Guessing Game Two
In a previous exercise, we’ve written a program that “knows” a number and
asks a user to guess it.
This time, we’re going to do exactly the opposite. You, the user, will have
in your head a number between 0 and 100. The program will guess a number,
and you, the user, will say whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how many
guesses it took to get your number.

As the writer of this program, you will have to choose how your
program will strategically guess. A naive strategy can be to simply
start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit
the number. But that’s not an optimal guessing strategy. An alternate
strategy might be to guess 50 (right in the middle of the range),
and then increase / decrease by 1 as needed. After you’ve written
the program, try to find the optimal strategy!
(We’ll talk about what is the optimal one next week with the solution.)
"""

start = 0
end = 100
guess_num = 0
answers = ("correct", "lower", "greater")

while True:
    guess_num += 1
    mid = (start + end)//2
    print(f"Computer number: {mid:.0f}")
    while True:
        user_answer = input("Is it the correct number? "
                            "Please type correct/lower/greater: ")
        if user_answer.lower() in answers:
            break
        else:
            print("It's not appropriate value. Try again!")

    if user_answer.lower() == "correct":
        print(f"Computer guessed the number. Attempts: {guess_num}")
        break
    elif user_answer.lower() == "lower":
        if mid == 100:
            print("You cheat! It's maximum number")
            break
        start = mid + 1
    else:
        if mid == 0:
            print("You cheat! It's minimum number")
            break
        end = mid - 1

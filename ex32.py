"""
Exercise 32: Hangman
This exercise is Part 3 of 3 of the Hangman exercise series.
The other exercises are: Part 1 and Part 2.

You can start your Python journey anywhere, but to finish this exercise you
will have to have finished Parts 1 and 2 or use the solutions (Part 1 and
Part 2).

In this exercise, we will finish building Hangman. In the game of Hangman,
the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms)
before they lose the game.

In Part 1, we loaded a random word list and picked a word from it. In Part 2,
we wrote the logic for guessing the letter and displaying that information to
the user. In this exercise, we have to put it all together and add logic for
handling guesses.

Copy your code from Parts 1 and 2 into a new file as a starting point. Now add
the following features:
Only let the user guess 6 times, and tell the user how many guesses they have
left.
Keep track of the letters the user guessed. If the user guesses a letter they
already guessed, don’t penalize them - let them guess again.

Optional additions:
When the player wins or loses, let them start a new game.
Rather than telling the user "You have 4 incorrect guesses left", display some
picture art for the Hangman. This is challenging - do the other parts of the
exercise first!
Your solution will be a lot cleaner if you make use of functions to help you!
"""
import random


def random_word():
    word_list = [line.rstrip('\n') for line in open("sowpods.txt", "r")]
    word = random.sample(word_list, 1)
    return word


def hangman():
    guessed_letter = set()
    count = 0
    wrong_guess = 6
    clue_word = random_word()[0]
    print(clue_word)

    while True:
        letter = input("What is your letter: ").upper()
        if letter in guessed_letter:
            print("You chose this letter before!")
            continue
        count += 1
        guessed_letter.add(letter)
        for letters in clue_word:
            if letters in guessed_letter:
                print(letters, end="")
            else:
                print("_", end="")
        print("")
        if letter not in clue_word:
            wrong_guess -= 1
            if wrong_guess == 0:
                print("You lost!")
                break
            else:
                print(f"You have only {wrong_guess} attempts left!")
        if set(clue_word) == guessed_letter.intersection(set(clue_word)):
            print(f"You guessed correctly! You needed {count} attempts")
            break


if __name__ == "__main__":
    while True:
        hangman()
        answer = input("Do you want to play again? Y/N: ")
        if answer.upper() == "Y":
            continue
        else:
            break

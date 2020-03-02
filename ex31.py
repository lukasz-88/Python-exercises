"""
Exercise 31: Guess Letters
This exercise is Part 2 of 3 of the Hangman exercise series.
The other exercises are: Part 1 and Part 3.

Let’s continue building Hangman. In the game of Hangman, a clue word
is given by the program that the player has to guess, letter by letter.
The player guesses one letter at a time until the entire word has been
guessed. (In the actual game, the player can only guess 6 letters incorrectly
before losing).

Let’s say the word the player has to guess is “EVAPORATE”. For this exercise,
write the logic that asks a player to guess a letter and displays letters in
the clue word that were guessed correctly. For now, let the player guess
an infinite number of times until they get the entire word. As a bonus, keep
track of the letters the player guessed and display a different message if
the player tries to guess that letter again. Remember to stop the game when
all the letters have been guessed correctly! Don’t worry about choosing a
word randomly or keeping track of the number of guesses the player has
remaining - we will deal with those in a future exercise.

An example interaction can look like this:
Welcome to Hangman!
_ _ _ _ _ _ _ _ _
Guess your letter: S
Incorrect!
Guess your letter: E
E _ _ _ _ _ _ _ E
...
And so on, until the player gets the word.
"""

clue_word = "EVAPORATE"
guessed_letter = set()
count = 0

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
    if set(clue_word) == guessed_letter:
        print(f"You guessed correctly! You needed {count} attempts")
        break

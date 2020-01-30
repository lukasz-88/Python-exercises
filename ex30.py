"""
Exercise 30: Pick Word
This exercise is Part 1 of 3 of the Hangman exercise series.
The other exercises are: Part 2 and Part 3.
In this exercise, the task is to write a function that picks a random word
from a list of words from the SOWPODS dictionary. Download this file and save
it in the same directory as your Python code. This file is Peter Norvig’s
compilation of the dictionary of words used in professional Scrabble
tournaments. Each line in the file contains a single word.

Hint: use the Python random library for picking a random word.
"""
import random


def random_word():
    word_list = [line.rstrip('\n') for line in open("sowpods.txt", "r")]
    word = random.sample(word_list, 1)
    return word


print(random_word())

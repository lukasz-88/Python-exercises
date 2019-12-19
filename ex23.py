"""
Exercise 23: File Overlap
Given two .txt files that have lists of numbers in them, find the numbers
that are overlapping. One .txt file has a list of all prime numbers
under 1000, and the other .txt file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any
other number. And yes, happy numbers are a real thing in
mathematics - you can look it up on Wikipedia. The explanation is easier
with an example, which I will describe below.)
"""

import pprint

happy_num = set()
prime_num = set()

with open("happynumbers.txt", "r") as file_1:
    for line in file_1:
        number = int(line.strip("\n"))
        happy_num.add(number)

with open("primenumbers.txt", "r") as file_2:
    for line in file_2:
        number = int(line.strip("\n"))
        prime_num.add(number)

pprint.pprint(sorted(prime_num.intersection(happy_num)))

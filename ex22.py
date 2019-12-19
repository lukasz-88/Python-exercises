"""
Exercise 22: Read From File
Given a .txt file that has a list of a bunch of names, count how many
of each name there are in the file, and print out the results to the screen.
I have a .txt file for you, if you want to use it! (nameslist.txt)

Extra:
Instead of using the .txt file from above (or instead of, if you want
the challenge), take this .txt file (Training_01.txt), and count how many
of each “category” of each image there are. This text file is actually a list
of files corresponding to the SUN database scene recognition database,
and lists the file directory hierarchy for the images. Once you take a look
at the first line or two of the file, it will be clear which part
represents the scene category. To do this, you’re going to have to remember
a bit about string parsing in Python 3. I talked a little bit about it in
this post.
"""

""" basic exercise:

names = dict()

with open("nameslist.txt", "r") as file:
    for line in file:
        name = line.strip("\n")
        if name in names:
            names[name] += 1
        else:
            names[name] = 1

print(sorted(names.items(), key=lambda names: names[1], reverse = True))
"""


"""extra:"""
import pprint

categories = dict()

with open("Training_01.txt", "r") as file:
    for line in file:
        category = line.split("/")[2]
        if category in categories:
            categories[category] += 1
        else:
            categories[category] = 1

pprint.pprint(sorted(categories.items(), key=lambda categories: categories[1], reverse=True))

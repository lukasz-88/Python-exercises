"""
Exercise 24: Draw A Game Board
This exercise is Part 1 of 4 of the Tic Tac Toe exercise series.
The other exercises are: Part 2, Part 3, and Part 4.

Time for some fake graphics! Let’s say we want to draw game boards
that look like this:
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
This one is 3x3 (like in tic tac toe). Obviously, they come in many other
sizes (8x8 for chess, 19x19 for Go, and many more).
Ask the user what size game board they want to draw, and draw it for them
to the screen using Python’s print statement.

Remember that in Python 3, printing to the screen is accomplished by
print("Thing to show on screen")
Hint: this requires some use of functions, as were discussed
previously on this blog and elsewhere on the Internet, like this
TutorialsPoint link.
"""


def board(n):

    print(" ---"*n)
    for i in range(n):
        print("|" + "   |"*n)
        print(" ---"*n)


if __name__ == "__main__":
    while True:
        user_ans = input("What's size you would like to draw? ")
        if user_ans.isnumeric() is True and int(user_ans) > 0:
            break
        else:
            print("Incorrect answer!")
            continue
    board(int(user_ans))

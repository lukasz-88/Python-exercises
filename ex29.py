"""
Exercise 29: Tic Tac Toe Game
This exercise is Part 4 of 4 of the Tic Tac Toe exercise series.
The other exercises are: Part 1, Part 2, and Part 3.

In 3 previous exercises, we built up a few components needed to build a
Tic Tac Toe game in Python:
1)Draw the Tic Tac Toe game board
2)Checking whether a game board has a winner
3)Handle a player move from user input
The next step is to put all these three components together to make a
two-player Tic Tac Toe game! Your challenge in this exercise is to use the
functions from those previous exercises all together in the same program to
make a two-player game that you can play with a friend. There are a lot of
choices you will have to make when completing this exercise, so you can go
as far or as little as you want with it.

Here are a few things to keep in mind:
- You should keep track of who won - if there is a winner, show a
congratulatory message on the screen.
- If there are no more moves left, don’t ask for the next player’s move!
As a bonus, you can ask the players if they want to play again and keep a
running tally of who won more - Player 1 or Player 2.
"""
import re

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

player_sign = {"one": "X", "two": "O"}
player_current = player_sign["one"]
counter = 0


def board(n):
    print(" ---"*n)
    for i in range(n):
        for j in range(n):
            print("|" + f" {game[i][j]} ", end='')
        print("|")
        print(" ---"*n)


def check_tic_tac_toe(board_game):
    result = 'draw'
    player = ''
    while True:
        for i in range(3):
            if board_game[0][i] == board_game[1][i] and \
                    board_game[1][i] == board_game[2][i] and \
                    board_game[0][i] != 0:
                result = 'win'
                player = board_game[0][i]
                break
        for j in range(3):
            if board_game[j][0] == board_game[j][1] and \
                    board_game[j][1] == board_game[j][2] and \
                    board_game[j][0] != 0:
                result = 'win'
                player = board_game[j][0]
                break
        if board_game[0][0] == board_game[1][1] and \
                board_game[1][1] == board_game[2][2] and \
                board_game[1][1] != 0:
            result = 'win'
            player = board_game[1][1]
            break
        elif board_game[2][0] == board_game[1][1] and \
                board_game[1][1] == board_game[0][2] and \
                board_game[1][1] != 0:
            result = 'win'
            player = board_game[1][1]
            break
        else:
            break
    return [result, player]


def gameboard_player(gameboard_1, gameboard_2, player):
    game[gameboard_1][gameboard_2] = player


def player_answer():
    while True:
        answer = str(input("What is your move? Please type appropriate number "
                           "between 1-3 in format: 'row,column': "))
        if re.search("[1-3],[1-3]", answer):
            if game[int(answer[0]) - 1][int(answer[-1]) - 1] != 0:
                print("This move has already been made.")
                print("Try again, choose your move: ")
                continue
            else:
                gameboard_player(int(answer[0]) - 1, int(answer[2]) - 1, player_current)
                break
        else:
            print("Wrong input, try again!")
            continue


def player_change(player_num):
    if player_num == "X":
        return player_sign["two"]
    else:
        return player_sign["one"]


while True:
    if counter != 9:
        player_answer()
        counter += 1
        board(3)
        check_result = check_tic_tac_toe(game)
        if check_result[0] == "win":
            if check_result[1] == "X":
                print("The winner is player one")
            else:
                print("The winner is player two")
            break
        player_current = player_change(player_current)
    else:
        print("No more valid moves")
        print("Result: draw")
        break

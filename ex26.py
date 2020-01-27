# coding=utf-8
"""
Exercise 26: Check Tic Tac Toe
This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other
exercises are: Part 1, Part 3, and Part 4. As you may have guessed, we are
trying to build up to a full tic-tac-toe board. However, this is significantly
more than half an hour of coding, so we’re doing it in pieces.Today, we will
simply focus on checking whether someone has WON a game of Tic Tac Toe,
not worrying about how the moves were made. If a game of Tic Tac Toe is
represented as a list of lists, like so:
game = [[1, 2, 0],
    	[2, 1, 0],
	    [2, 1, 1]]
where a 0 means an empty square, a 1 means that player 1 put their token in
that space, and a 2 means that player 2 put their token in that space. Your
task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe
game board, tell me whether anyone has won, and tell me which player won,
if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or
a diagonal. Don’t worry about the case where TWO people have won - assume
that in every board there will only be one winner. Here are some more examples
to work with:
winner_is_2 = [[2, 2, 0],
              [2, 1, 0],
	         [2, 1, 1]]
winner_is_1 =   [[1, 2, 0],
        	    [2, 1, 0],
	            [2, 1, 1]]
winner_is_also_1 = [[0, 1, 0],
                	[2, 1, 0],
	                [2, 1, 1]]
no_winner = [[1, 2, 0],
        	[2, 1, 0],
	        [2, 1, 2]]
also_no_winner = [[1, 2, 0],
            	[2, 1, 0],
	            [2, 1, 0]]
"""

game = [[0, 0, 1],
        [0, 1, 0],
        [1, 0, 0]]


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


print(check_tic_tac_toe(game))

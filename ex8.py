"""
Exercise 8: Rock Paper Scissors
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner, and ask
if the players want to start a new game)

Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock
"""

choice = ('rock', 'scissors', 'paper')


def player_choice(number):
    while True:
        player_ans = input("Player {}, enter rock/scissors/paper: ".format(number))
        if player_ans.lower() not in choice:
            continue
        else:
            break
    return player_ans.lower()

            
while True:
    player_1 = player_choice('One')
    player_2 = player_choice('Two')

    if player_1 == player_2:
        print("Draw")
    elif (player_1 == 'rock' and player_2 == 'scissors') \
            or (player_1 == 'scissors' and player_2 == 'paper') \
            or (player_1 == 'paper' and player_2 == 'rock'):
        print("The winner is player One.")
    else:
        print("The winner is player Two.")

    question = input("Do you want to play again? True/False: ")
    if question not in ['True', 'T', 'true', '1']:
        break


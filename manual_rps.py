import numpy as np
from random import choice

def get_computer_choice(actions: list) -> str:

    action = choice(actions)
    print(f"Computer action: {action}")

    return action

def get_player_choice(actions: list) -> str:

    action = ''
    while action not in actions:
        action = input("Choose your action: ").lower()
        action = action[0].upper() + action[1:]

    if action == 'Nothing': print("Hey! Choose your action.\n")

    return action

def get_winner(player_action: str, computer_action: str) -> int:

    if computer_action in lost_against[player_action]:

        print("\nThis time you win")
        won = 1

    elif player_action in lost_against[computer_action]:

        print("\nThis time computer won")
        won = -1

    else: 

        print("\nIt is a draw!")
        won = 0
    
    print("")

    return won

def play(actions: list, lost_against: dict):

    print("\nAll hail Sam Kass! Hail!\n")

    player_win_count = 0
    computer_win_count = 0
    game_continues = True

    while game_continues:

        player_action = get_player_choice(actions=actions + ['Nothing'])

        if player_action != 'Nothing':

            computer_action = get_computer_choice(actions=actions)
            won = get_winner(player_action=player_action, computer_action=computer_action)

            if won == 1: 
                player_win_count += 1
            elif won == -1:
                computer_win_count +=1

            game_continues = (player_win_count < 3 and computer_win_count < 3)

    if player_win_count == 3:

        print("Congrats. You won the entire game!")
    
    elif computer_win_count == 3:

        print("Computer won the game. So sorry!")

    print("")

actions = ['Rock','Paper','Scissors','Lizard','Spock']
lost_against = {
    'Rock': ['Lizard', 'Scissors'], 
    'Paper': ['Rock','Spock'], 
    'Scissors': ['Paper','Lizard'], 
    'Spock': ['Scissors','Rock'], 
    'Lizard': ['Spock', 'Paper'] 
    }

play(actions=actions, lost_against=lost_against)
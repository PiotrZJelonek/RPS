import numpy as np
from random import choice



def get_computer_choice(actions: list):
    return choice(actions)

def get_player_choice(actions: list):
    action = ''
    while action not in actions:
        action = input("Choose your action: ").lower()
        action = action[0].upper() + action[1:]
    return action


############

print("All hail Sam Kass! Hail!")

actions = ['Rock','Paper','Sciccors','Lizard','Spock']

computer_action = get_computer_choice(actions)

print(computer_action)

player_action = get_player_choice(actions)
print(player_action)

print("\n")

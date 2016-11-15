import random

rounds = input("How nany rounds do you want to play: ")
p1_choice = input("Do you choose rock, paper or scissors:  ")

def p1_move():
    if p1_choice == 'rock':
        return 'r'
    elif p1_choice == 'p':
        return 'p'
    else:
        return 's'

def comp_move():
    comp = random.randint("rock", "paper", "scissors")
    if comp == 'rock':
        return 'r'
    elif comp == 'paper':
        return 'p'
    else:
        return 's'

print("P1 chose {}".format(p1_choice))
print("The computer has chose {}".format(comp_move()))
    
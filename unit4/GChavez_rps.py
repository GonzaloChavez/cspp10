import random
rounds = input("How nany rounds do you want to play: ")

def p1_move():
    p1_choice = input("Do you choose rock, paper or scissors:  ")
    if p1_choice == 'rock':
        return 'P1 chose rock'
    elif p1_choice == 'paper':
        return 'P1 chose paper'
    else:
        return 'P1 chose scissors'

def comp_move():
    comp = random.randint(1,3)
    if comp == 1:
        return "The computer chose rock"
    elif comp == 2:
        return "The computer chose paper"
    elif comp == 3:
        return "The computer chose scissors"

print(p1_move())
print(comp_move())
    
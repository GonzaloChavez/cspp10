import random

def get_p1_move(rock, paper, scissors):
    p1_move = input("Do you choose rock, paper or scissors:  ")
    if p1_move == 'rock':
        return 'P1 chose rock'
    elif p1_move == 'paper':
        return 'P1 chose paper'
    else:
        return 'P1 chose scissors'

def get_comp_move(rock,paper, scissors):
    comp_move = random.randint(1,3)
    if comp_move == 1:
        return "The computer chose rock"
    elif comp_move == 2:
        return "The computer chose paper"
    elif comp_move == 3:
        return "The computer chose scissors"
        
def get_rounds():
    rounds = int(input("How many rounds do you want to play from 1 to 9: "))
    if rounds <= 9:
        return rounds
    else:
        print("Too many rounds")

def get_round_winner(p1_move, comp_move):
    if p1_move == "rock" and comp_move == "paper":
        return "The computer wins"
    elif p1_move == "rock" and comp_move == "scissors":
        return "P1 wins"
    elif p1_move == "rock" and comp_move == "rock":
        return "It's a tie"
    elif p1_move == "paper" and comp_move == "rock":
        return "P1 wins"
    elif p1_move == "paper" and comp_move == "scissors":
        return "The computer wins"
    elif p1_move == "paper" and comp_move == "paper":
        return "It's a tie"
    elif p1_move == "scissors" and comp_move == "rock":
        return "The computer wins"
    elif p1_move == "scissors" and comp_move == "paper":
        return "P1 wins"
    elif p1_move == "scissors" and comp_move == "scissors":
        return "It's a tie"

#print(get_p1_move())
#print(get_comp_move())
#print(get_rounds())
print(get_round_winner(get_p1_move,get_comp_move))
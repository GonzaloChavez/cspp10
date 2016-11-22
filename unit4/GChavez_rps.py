import random


def get_p1_move():
    p1_move = input("Do you choose rock, paper or scissors:  ")
    if p1_move == "rock":
        return 'r'
    elif p1_move == "paper":
        return "p"
    else:
        return "s"

def get_comp_move():
    comp_move = random.randint(1,3)
    if comp_move == 1:
        return "r"
    elif comp_move == 2:
        return "p"
    elif comp_move == 3:
        return "s"
        
def get_rounds():
    rounds = int(input("How many rounds do you want to play from 1 to 9: "))
    if rounds <= 9:
        return rounds
    else:
        print("Too many rounds")

def get_round_winner(p1_move, comp_move):
    if p1_move == "r" and comp_move == "p":
        return "The computer wins"
    elif p1_move == "r" and comp_move == "s":
        return "P1 wins"
    elif p1_move == "r" and comp_move == "r":
        return "It's a tie"
    elif p1_move == "p" and comp_move == "r":
        return "P1 wins"
    elif p1_move == "p" and comp_move == "s":
        return "The computer wins"
    elif p1_move == "p" and comp_move == "p":
        return "It's a tie"
    elif p1_move == "s" and comp_move == "r":
        return "The computer wins"
    elif p1_move == "s" and comp_move == "p":
        return "P1 wins"
    elif p1_move == "s" and comp_move == "s":
        return "It's a tie"

def get_full_move(shortmove):
    if shortmove == 'r':
        return "rock"
    elif shortmove == 'p':
        return "paper"
    elif shortmove == 's':
        return "scissors"
        
def print_score(pscore, cscore, ties):
        return("Player Wins: {} Computer Wins: {} Ties: {}" .format(pscore, cscore, ties))
    
        
def rps():
    rounds = get_rounds()
    
    p1move = get_p1_move()
    compmove = get_comp_move()
    
    print("Player chose {}".format( get_full_move(p1move)))
    print("The computer chose {}".format( get_full_move(compmove) ) )
    
    winner = get_round_winner(p1move,compmove)
    if winner == "players":
        print("Player1 won")
        
    elif winner == "comp":
        print("The Computer won")
        
    else:
        print("It's a tie")
    
#print(get_rounds())
#print(get_p1_move())
#print(get_comp_move())
print(get_round_winner(p1move, cmove))
#print(get_full_move())
#print(print_score()
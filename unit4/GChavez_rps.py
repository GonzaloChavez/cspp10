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
    return rounds

def get_round_winner(p1_move, comp_move):
    if p1_move == "r" and comp_move == "p":
        return "computer"
    elif p1_move == "r" and comp_move == "s":
        return "player"
    elif p1_move == "r" and comp_move == "r":
        return "tie"
    elif p1_move == "p" and comp_move == "r":
        return "player"
    elif p1_move == "p" and comp_move == "s":
        return "computer"
    elif p1_move == "p" and comp_move == "p":
        return "tie"
    elif p1_move == "s" and comp_move == "r":
        return "computer"
    elif p1_move == "s" and comp_move == "p":
        return "player"
    elif p1_move == "s" and comp_move == "s":
        return "tie"

def get_full_move(shortmove):
    if shortmove == 'r':
        return "rock"
    elif shortmove == 'p':
        return "paper"
    elif shortmove == 's':
        return "scissors"
        
def print_score(pscore, cscore, ties):
        return("Player Wins: {}\nComputer Wins: {}\nTies: {}".format(pscore, cscore, ties))
    
def rps():
    rounds = get_rounds()
    
    pscore = 0
    cscore = 0
    ties = 0
    
    for x in range(rounds):
        p1move = get_p1_move()
        compmove = get_comp_move()
    
        print("Player chose {}".format( get_full_move(p1move)))
        print("The computer chose {}".format( get_full_move(compmove) ) )
    
        winner = get_round_winner(p1move,compmove)
        if winner == "player":
            print("Player1 won")
            pscore = pscore + 1
        
        elif winner == "computer":
            print("The Computer won")
            cscore = cscore + 1
            
        elif winner == "tie":
            print("It's a tie")
            ties = ties + 1
        print(print_score(pscore, cscore, ties))
        print("-------------------")
        
    if pscore > cscore:
        print("Player1 Has Defeated The Computer!")
    elif cscore > pscore:
        print("The Computer Has Defeated Player1!")
    else:
        print("You Both Tie, So You Both Lose!")
        
rps()

import random
bank = 100 
# function for rolling 2 dice
# name: roll2dice
# arguments: none
# returns: the sum
def roll2dice():
    # generate a random number from 1 to 6
    dice_1 = random.randint(1,6)
    # generate another random number from 1 to 6
    dice_2 = random.randint(1,6)
    # get the sum of the two rolls
    dice_sum = dice_1 + dice_2
    # print the sum
    print(dice_sum)
    # return the sum
    return dice_sum
    
# function for getting a user's bet
# name: get_bet
# arguments: bank - current player balance
# returns: the bet
def get_bet(bank):
    # ask the player how much they want to bet
    bet = int(input("Bank Acc: 100, How Much Do You Want To Bet? "))
    # if player's bet is more than they have
    #   available in bank, then get new bet
    while True:
        if bet < 0:
            print("No negative numbers")
            
        elif bet > bank:
            print("You Don't Have That Kind Of Money!")
                  
        elif bet <= bank:
            return bet

        bet = int(input("Bank Acc: 100, How Much Do You Want To Bet: "))  
        
        
    # if player's bet is valid, then return
    #   the bet
 
# function that finds the range given a dice roll
# name: get_range
# arguments: sum of dice
# returns: the range:
#           "over7" if over 7
#           "under7" if under 7
#           "equal7" if equal to 7
def get_range(dice_sum):
    # if the sum is over 7, return "over7"
    if dice_sum > 7:
        return("over7")
    # if the sum is under 7, return "under7"
    elif dice_sum < 7:
        return("under7")
    # if the sum is 7, return "equal7"
    elif dice_sum == 7:
        return("equal7")
        
# function for getting the user's choice of range
# name: choose_range
# arguments: none
# returns: player's choice of range
#       "over7", "under7", or "equal7"
def choose_range():
    # present user with choices "over7", "under7",
    #   or "equal7"
    choice = input("Choose: over7 or under7 or equal7 ? ")
    # return their choice
    return choice
    
# function for the main game
def overunder7():
    bet = get_bet(bank)
    
overunder7()
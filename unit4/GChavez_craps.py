import random
bank_amount = 100
print("Welcome to Craps, you have $100 in your bank")

def get_bet(bank_amount):
    bet = int(input("How much do you want to bet: "))
    while True:
        if bet < 0:
            print("No negative numbers")
            
        elif bet <= bank_amount:
            return bet
            
        elif bet > bank_amount:
            print("You don't have that kind of money")

        bet = int(input("Bank Acc: 100, How much do you want to bet: "))
        
def get_roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("Dice 1: {} Dice 2: {}\nDice Sum: {}".format(dice1, dice2, dice_sum))
    return dice_sum

def get_first_roll(dice_sum):
    if (dice_sum == 2) or (dice_sum == 3) or (dice_sum == 12):
        print("You Lose!")
        return 'lose'
    
    elif (dice_sum == 7) or (dice_sum ==  11):
        print("You Won!")
        return 'win'
    
    else:
        return dice_sum

#function name: update_bank
#purpose: change bank amount based on whether the player won or not
#arguments:
#   bet - what the player bet
#   bank_amount - how much the player has in their bank
#   result - what happened in the round
#returns: the updated amount in the bank

def get_update_bank(bet, bank_amount, result):
    if result == 'lose':
        bank_amount = bet - bet
        print("You Lost! Bank Amount: {}".format(bank_amount))

    elif result == 'win':
        bank_amount = bet + bet
        print("You Won! Bank Amount: {}".format(bank_amount)) 
    return bank_amount
        
def get_second_roll(dice_sum):
    new_dice1 = random.randint(1,6)
    new_dice2 = random.randint(1,6)
    new_dice_sum = new_dice1 + new_dice2 
    if new_dice_sum != 7 or  new_dice_sum != dice_sum:
        while new_dice_sum != 7 or  new_dice_sum != dice_sum:
            print("Dice 1: {} Dice 2: {}\nDice Sum: {}".format(new_dice1, new_dice2, new_dice_sum))
            break
        
    elif new_dice_sum == 7 or new_dice_sum == dice_sum:
        print("You Win")
        
def craps():
    bank_amount = 100
    bet = get_bet(bank_amount)
    roll2dice = get_roll2dice()
    dice_sum = roll2dice
    firstroll = get_first_roll(dice_sum)
    secondroll = get_second_roll(dice_sum)

    while bank_amount > 0:
        if dice_sum == 'lose':
            bank_amount = bet-bet
            print("You Lose! Bank Amount: {}".format(bank_amount))
        elif dice_sum == 'win':
            bank_amount = bet + bet
            print("You Win! Bank Amount: {}".format(bank_amount))
        elif dice_sum == dice_sum:
            break
        
    print("Your Point Nunber: {}".format(dice_sum))
    
#if new_dice_sum == dice_sum:
        
            
    

craps()
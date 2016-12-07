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
        
def roll2diceO():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("Dice 1: {} Dice 2: {}".format(dice1, dice2))
    return dice_sum

    
    
get_bet(bank_amount)
roll2diceO()
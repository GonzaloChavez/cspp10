opt = input("Would you rather Withdraw, Deposit, or Exit: ")
money = 10000

while money > 0:
        if opt == ("Withdraw"):
            w = int(input("How much do you want to take out: "))
            if (w > money):
                print("You don't have that kind of money")
            elif (w <= money):
                money = money - w
                print(money)
                break
        
        elif opt == ("Deposit"):
            d = int(input("How much do you want to put in: "))
            money = money + d
            print(money)
            break
        
        elif opt == ("Exit"):
            break
        

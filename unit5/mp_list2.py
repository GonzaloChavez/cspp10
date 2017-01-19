#Worked With Andres
num = []
while True:
    user_input = input("Number? Sum? Clear? Print? Length? Exit? ")

    if user_input == "Sum":
        print(sum(num))
    
    elif user_input == "Clear":
        num = []
        print(num)

    elif user_input == "Print":
        print(num)
        
    elif user_input == "Length":
        for index in range(len(num)):
	        print("{} At Index {}".format(num[index],index))

    elif user_input == "Exit":
        print("Done")
        break
        
    else:
        num.insert(0, int(user_input))
#Worked With Andres
num = []
while True:
    user_input = input("Number? Sum? Clear? Print? Length? Exit? ")
    num.insert(0, user_input)

    #if user_input == "Sum":
        
    

    if user_input == "Clear":
        num = []
        print(num)

    elif user_input == "Print":
        print(num)
        
    elif user_input == "Length":
        for index in range(len(num)):
	        print("{} at index {}".format(num[index],index))

    elif user_input == "Exit":
        print(num)
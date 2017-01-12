num = []
num_choice = 1
while num_choice != 0:
    user_input = int(input("Enter any number: "))
    
    if user_input >= 1:
        num.insert(0, user_input)
    
    if user_input < 0:
        if (user_input * -1) in num:
            num.remove(user_input * -1)

    if user_input == 0:
        print("End")

    print(num)
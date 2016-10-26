#This asks the user to type in something. In this case, an equation
user_equation = input("Enter a equation ")

#We want to get the equation separated for each index
num_1 = user_equation[0]
operator = user_equation[1]
num_2 = user_equation[2]

#We use the if,elif and else statements to excatly get the sign of the equation corect and then printing the equation
if operator == "+":
    solution_0 = int(num_1) + int(num_2)
    print("The result is {}".format(solution_0))
    
elif operator == "-":
    solution_1 = int(num_1) - int(num_2)
    print("The result is {}".format(solution_1))
    
elif operator == "*":
    solution_2 = int(num_1) * int(num_2)
    print("The result is {}".format(solution_2))
    
elif operator == "/":
    solution_3 = int(num_1) / int(num_2)
    print("The result is {}".format(solution_3))
    
else:
    solution_4 = int(num_1) % int(num_2)
    print("The result is {}".format(solution_4))    


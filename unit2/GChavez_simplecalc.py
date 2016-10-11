user_equation = input("Enter a equation ")
num_1 = user_equation[0]
operator = user_equation[1]
num_2 = user_equation[2]

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


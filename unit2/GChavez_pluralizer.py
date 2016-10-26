#Here, we asking the user to enter two things
num = input("Enter a number: ")
noun = input("Enter a noun: ")

#We use the if statement to get 1 out the way 
if num == "1":
    print("1 " + noun)
#We used the else and then start using the if,elif and else again to get the exact letters in a word and taking it out to exchange them    
else:
    if noun[-2:] == "fe":
        print(num + " " + noun[:-2] + "ves") 
        
    elif noun[-2:] == "ay" or noun[-2:] == "uy" or noun[-2:] == "oy" or noun[-2:] == "ey":
        print(num + " " + noun + "s")

    elif noun[-1] == "y":
        print(num + " " + noun[:-1] + "ies")
 
    elif noun[-2:] == "sh" or noun[-2:] ==  "ch":
        print(num + " " + noun + "es")

    elif noun[-2:] == "us":
        print(num + " " + noun[:-2] + "i")
    else: 
        print (num + " " + noun + "s")


    
    
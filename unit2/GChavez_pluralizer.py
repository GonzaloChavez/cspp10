num = input("Enter a number: ")
noun = input("Enter a noun: ")

if num == "1":
    print("1 " + noun)
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


    
    
num = input("Enter a number ")
noun = input("Enter a noun ")

if int(num) == 0 and int(num) > 1 or noun[-2:] == "fe":
    print(str(num) + str(noun[:-2]) + "ves")
elif int(num) == 1:
    print(str(num) + noun)
    
elif int(num) == 0 and int(num) > 1 or noun[-1:] == "y":
    print(str(num) + str(noun[:-1]) + "ies")
elif int(num) == 1:
    print(str(num) + noun)
    
elif int(num) == 0 and int(num) > 1 or noun[-2:] == "sh" or "ch":
    print(str(num) + str(noun) + "es")
elif int(num) == 1:
    print(str(num) + noun)
    
elif int(num) == 0 and int(num) > 1 or noun[-2:] == "us":
    print(str(num) + str(noun[:-2]) + "i")
elif int(num) == 1:
    print(str(num) + noun)
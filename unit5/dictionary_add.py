from pprint import pprint

d = {
}
user_input = input("Add? Remove Key? Update? Print? Exit? ")
    
def Add(user_input):
        if user_input == "Add":
            key = input("Enter A Key ")
            value = input("Enter A Value ")
            d[key] = value
            print(d)

def RemoveKey(user_input):
    if user_input == "Remove Key":
        delete = input("What Key Do You Want To Delete? ")
        del d[delete]
    
def Update(user_input):
    if user_input == "Update":
        update = input("What Key Do You Want To Update? ")
        new_update = input("What Do You Want It To Update To? ")
        d[update] = new_update

def Print(user_input):
    if user_input == "Print":
        pprint(d)
def Exit(user_input):
    if user_input == "Exit":
        print("Done")
 

def dictionary():
    while user_input != "Exit":
        Add(user_input)
        RemoveKey(user_input)
        Update(user_input)
        Print(user_input)
    Exit(user_input)
        
dictionary()
from pprint import pprint

d = {
}

def user_choice():
    user_input = input("Add? Remove Key? Update? Print? Exit? ")
    
def Add(user_choice):
    if user_input == "Add":
        key = input("Enter A Key ")
        value = input("Enter A Value ")
        d[key] = value
        pprint(d)

def RemoveKey(user_choice):
    if user_input == "Remove Key":
        del d[input]
        pprint(d)
    
def Update(user_choice):
    if user_input == "Update":
        d[input] = input
        pprint(d)

def Print(user_choice):
    if input == "Print":
        print(d)

def Exit(user_choice):
    if input == "Exit":
        print("Done")
        break

def dictionary():
    
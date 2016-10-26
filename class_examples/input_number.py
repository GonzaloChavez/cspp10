# program will take in a bunch of numbers
# until the user types "eit" and then 
# prints out all the numbers together

final = ""
inp = input("Enter a number or exit: ")
while (inp != "exit"):
    inp = input("Enter a number or exit: ")
    final = final + inp + ""
print(final)
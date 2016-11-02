import random
num = random.randint(1,101)
guess = int(input("Enter a guess between 1-100: "))

while guess != num:
    
    if guess < num:
        print("Too Low")
        guess = int(input("Guess again: "))
        
    elif guess > num:
        print("Too High")
        guess = int(input("Guess again: "))
        
if guess == num:
    print("You got it! It was indeed {}".format(num))
 


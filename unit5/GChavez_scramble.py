import random
#function to scramble a single word
#name: scramble_word
#arguments: none
#returns: the scramble word 
def scramble_word():
    user_input = input("Enter a word: ")
    some_list = list(user_input)
    random.shuffle(some_list)
    print(some_list)
#function to scramble a series of words
#name: scramble_phase
#arguments: scramble_word
#returns: a series of words that are scramble
#def scramble_phase():

scramble_word()
import random

#function to scramble a single word where the first letter always stay the same
#name: scramble_word
#arguments: none
#returns: the scramble word 
def scramble_word():
    word_1 = input("Enter a word: ")
    num = 0
    some_list = list(word_1)
    random.shuffle(some_list)
    print(some_list)
#function to scramble a series of words
#name: scramble_phase
#arguments: scramble_word
#returns: a series of words that are scramble
def scramble_phase(scramble_word):
    user_input2 = input("Enter a sentence ")

scramble_word()
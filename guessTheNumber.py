# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui
import math

rang = 100
# helper function to start and restart the game
def new_game():
    """starts a new game getting a new random number"""
    global secret_number
    secret_number = random.randrange(0,rang)
    print "New game. Range is [0,", rang, ")"
    print "Remaining guesses = ", guesses()
    
def guesses():
#helper function to calculate the remaining guesses mathematically
    global remaining_guesses 
    remaining_guesses = round(math.log(rang, 2))
    return remaining_guesses
    
    
# define event handlers for control panel
def range100():
    """sets range == 100"""
    global rang 
    global remaining_guesses
    rang = 100
    remaining_guesses = 7
    new_game()


def range1000():
    """sets range == 1000"""    
    global rang 
    global remaining_guesses
    rang = 1000
    remaining_guesses = 10
    new_game()
    
def input_guess(guess):
    """ enter a new guess"""
    global number
    global remaining_guesses
    number = int(guess)
    remaining_guesses = remaining_guesses - 1
    print "You tried the number:", number, "remaining guesses =", remaining_guesses
    
    """Compares the entered number and prints out an 
    appropriate message"""
    if (number < secret_number) and (remaining_guesses >0): print "Higher"
    
    elif (number > secret_number) and (remaining_guesses >0): print "Lower"
    
    elif (number == secret_number) and (remaining_guesses >=0): 
        print "Correct!"
        new_game()
    
    else: 
        print "You ran out of guesses.  The number was", secret_number
        new_game()
    
# create frame
frame = simplegui.create_frame("Guess The Number",300,300)



# register event handlers for control elements and start frame
frame.add_input("Number:", input_guess, 100)
frame.add_button("100", range100, 100)
frame.add_button("1000", range1000, 100)


# call new_game 
new_game()


#You can test this code at: http://www.codeskulptor.org/#user40_2PlCDCJRlQrLilm.py

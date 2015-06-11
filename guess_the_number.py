# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# helper function to start and restart the game
def new_game():
    global secret_number
    global user_guess
    global guess
    global Numguess
    Numguess = 7
    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses is %s" % (Numguess) 
    secret_number = random.randrange(0,100)


# define event handlers for control panel
def range100():
    secret_number = random.randrange(0,100)

def range1000():
    secret_number = random.randrange(0,1000)
    
def input_guess(guess):
    guess = int(guess)
    global Numguess
    Numguess = Numguess - 1
    if (secret_number < guess):
        print "Too High!"
        print "Number of remaining guesses is %s" % (Numguess)
    elif (secret_number > guess):
        print "Too Low!"
        print "Number of remaining guesses is %s" % (Numguess)
    elif (secret_number == guess):
        print "Correct!"
    else:
        print "Are you sure you entered a number?"
        
   

    
# create frame
frame = simplegui.create_frame("Guess That #", 300, 200)

# register event handlers for control elements and start frame
frame.add_button("New Game [ 0 , 100 )", range100, 200)
frame.add_button("New Game [ 0 , 1000 )", range1000, 200)      
frame.add_input("Guess: ", input_guess, 200)
frame.add_button("Submit Guess ", input_guess, 200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric

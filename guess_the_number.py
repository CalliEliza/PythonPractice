# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# helper function to start and restart the game
def new_game():
    global secret_number
    global secret_number2
    global user_guess
    global guess
    global Numguess
    Numguess = 7
    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses is %s" % (Numguess) 
    secret_number = random.randrange(0,100)
    print "\n"


# define event handlers for control panel
def range100():
    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses is %s" % (Numguess) 
    secret_number = random.randrange(0,100)

def range1000():
    global Numguess2 
    Numguess2 = 10
    print "New game. Range is from 0 to 1000"
    print "Number of remaining guesses is %s" % (Numguess2) 
    secret_number2 = random.randrange(0,1000)
    print "\n"
    
def input_guess(guess):
    guess = int(guess)
    print "Guess is %s" %(guess)
    global Numguess
    global Numguess2
    # if statment for guessing 1-100
    Numguess = Numguess - 1
    Numguess2 = Numguess2 - 1
    if (secret_number < guess):
        print "Too High!"
        print "Number of remaining guesses is %s" % (Numguess)
        print "\n"
    elif (secret_number > guess):
        print "Too Low!"
        print "Number of remaining guesses is %s" % (Numguess)
        print "\n"
    elif (secret_number == guess):
        print "Correct!"
        print "\n"
        return new_game()
    elif (Numguess == 0):
        print "No more guesses!"
        print "\n"
        return new_game()
    # if statements for 1-1000
    elif (secret_number2 < guess):
        print "Too High!"
        print "Number of remaining guesses is %s" % (Numguess2)
        print "\n"
    elif (secret_number2 > guess):
        print "Too Low!"
        print "Number of remaining guesses is %s" % (Numguess2)
        print "\n"
    elif (secret_number2 == guess):
        print "Correct!"
        print "\n"
        return new_game()
    elif (Numguess2 == 0):
        print "No more guesses!"
        print "\n"
        return new_game()
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


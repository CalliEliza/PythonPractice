# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random



# secret_number1 = random.randrange(0,100)
Numguess = 7
NumRangeMin1 = 0
NumRangeMax1 = 100
NumRangeMax2 = 1000
Game100 = True
global guess
# helper function to start and restart the game

def new_game():
    global secret_number
    Numguess = 7
    print "New game. Range is from %s to %s" % (NumRangeMin1, NumRangeMax1)
    print "Number of remaining guesses is %s" % (Numguess)
    secret_number = random.randrange(0,100)
    print "\n"


# define event handlers for control panel
def range100():
    global Numguess
    global secret_number
    Numguess = 7
    print "New game. Range is from %s to %s" % (NumRangeMin1, NumRangeMax1)
    print "Number of remaining guesses is %s" % (Numguess)
    secret_number = random.randrange(0,100)
    print "\n"


def range1000():
    global Numguess
    Numguess = 10
    Game100 = False
    print "New game. Range is from %s to %s" % (NumRangeMin1, NumRangeMax2)
    print "Number of remaining guesses is %s" % (Numguess)
    secret_number = random.randrange(0,1000)
    print "\n"

        
def input_guess(guess):
    global Numguess
    
    # sets guess to a number instead of a string
    guess = int(guess)
 
    print "Guess is %s" %(guess)
    
    # if statment for guessing 1-100
    Numguess = Numguess - 1
    if (secret_number == guess):
        print "Correct!"
        print "\n"
        return new_game()
    elif (Numguess == 0):
        print "Nope, No more guesses!"
        print "\n"
        return new_game()
    elif (secret_number < guess):
        print "Too High!"
        print "Number of remaining guesses is %s" % (Numguess)
        print "\n"
    elif (secret_number > guess):
        print "Too Low!"
        print "Number of remaining guesses is %s" % (Numguess)
        print "\n"
       
       


        


# create frame
frame = simplegui.create_frame("Guess That #", 300, 200)

# register event handlers for control elements and start frame
frame.add_button("New Game [ 0 , 100 )", range100, 200)
frame.add_button("New Game [ 0 , 1000 )", range1000, 200)
frame.add_input("Guess: ", input_guess, 200)

# call new_game
new_game()



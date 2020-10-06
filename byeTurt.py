"""
Created on Mon Oct  5 13:25:06 2020

@author: Dr. Z

This is a code snippet! Take the part of this code that works for you and add
it to your script (.py file). You will probably have to make some changes to 
get it work perfectly.


CLICK THE TURTLE TO GET IT TO DISAPPEAR.

"""
import turtle, random 

w=600
h=600
turtle.setup(w,h) # start with calling setup to turn on listeners
turtle.listen() # for keyboard listening

# =========DEFINE VARIABLES BELOW=========
panel=turtle.Screen()
running = True # for controlling the while loop

testTudine = turtle.Turtle() # example turtle, AKA Felicia ;) 

# =========DEFINE FUNCTIONS BELOW=========

# MODIFY - delete this comment block
# def replaceFunctionName(x,y):
#     '''This function is callback for a mouse click.'''
#     # add the code that you'd like to perform when clicking HERE
#     # if you want to do something at the location of the click, use the parameters x and y in your
#     # code wherever you need (ex: goto(x,y))
    
def byeTurt(x,y):
    '''Callback function to hide a SINGLE turtle when clicked. Takes x and y
    as parameters, which get values whenever the click happens.
    For deleting multiple turtles, see the listTurtles.example.'''
    testTudine.hideturtle() # MODIFY - you'll have to change this to your turtle's name.

# =========SET UP TURTLE(S) BELOW (color, size, shape, etc)=========

# INTERACTION FUNCTIONS BELOW 
# add onclick and onkey commands below. 

# notice that onclick is attached to the TURTLE, not the panel.
testTudine.onclick(byeTurt)


# =========ANIMATIONS BELOW=========
# code will execute in order within the loop
# while running:





# =========LISTENERS & CLEANUP =========
panel.mainloop() # keep listeners listening DO NOT DELETE
turtle.done() # cleanup whenever we exit the loop DO NOT DELETE.
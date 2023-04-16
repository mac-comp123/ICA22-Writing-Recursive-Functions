""" -------------------------------------------------

Recursion Writing Starter File

<Your name here>
"""

import turtle
import math
import random

# -----------------------------------------------------
# factorial example

def fact(n):
    """Recursive factorial function, just as an example."""
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
    

# -----------------------------------------------------
# spiralIn example

def testSpiral(size):
    """Test function to make it faster to test the drawSpiral function"""
    scr = turtle.Screen()
    matsos = turtle.Turtle()
    spiralIn(matsos, size)
    scr.exitonclick()


def spiralIn(spiroTurt, sideLen):
    pass     # remove this and put your code here

    
# -----------------------------------------------------
# tree example
    
    
def treeMain(treeSize):
    """Tester function for the tree fractal."""
    myWin = turtle.Screen()
    t = turtle.Turtle()
    # set up turtle
    t.left(90)
    t.up()
    t.backward(treeSize + 25)
    t.down()
    t.speed(0)
    t.color("green")
    # draw the tree
    tree(treeSize,t)
    myWin.exitonclick()

def tree(branchLen,t):
    """The Interactive Textbook's tree drawing fractal function.
    Takes in the length of the main branch and a turtle, and it draws
    a symmetrical tree shape with branching to left and right. The fractal
    stops if the branch length gets to be less than or equal to 5"""
    if branchLen > 5:
        t.forward(branchLen)
        t.right(30)
        tree(branchLen-15,t)
        t.left(60)
        tree(branchLen-15,t)
        t.right(30)
        t.backward(branchLen)
    
    

# -----------------------------------------------------
# levyC example

    

def runLevy(reps):
    """A test function to make it easier to test the levyCFractal."""
    s = turtle.Screen()
    t = turtle.Turtle()
    # set up turtle to start
    t.up()
    t.left(90)
    t.backward(150)
    t.down()
    t.speed(0)
    # draw levyC fractal
    levyCFractal(t, 300, reps)
    s.exitonclick()
    

def levyCFractal(fran, size, reps):
    pass   # remove this and put your solution here


def nextSize(currSize):
    """Takes in the current straight-line length, and computes
    and returns the length of the isosceles triangle's side. """
    hDist = (currSize / 2)
    vDist = hDist * math.tan(math.radians(45))
    hypot = math.sqrt(vDist ** 2 + hDist ** 2)
    return hypot

  
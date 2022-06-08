#In this class, we will be going over the turtle module
from turtle import *
#Turtle is used to make cool graphics or art on a GUI

#Here is an example of a stary night sky

import random #we will need this to make random posistions for the stars

pensize(1) #Set the pensize very low
bgcolor("black") #Make the background of the window black
color("yellow") #Make the pen yellow
fillcolor("yellow") #Fill the shape with yellow
shape("arrow") #Make the pen into an arrow
speed(50) #Make the pen go fast


def makeStar():
    begin_fill() #Start filling the shape
    for i in range(5):
            forward(25) #Go forward 25 pixels
            right(144) #Rotate 144 degrees right
    end_fill() #Stop filling the shape

def makeMoon():
    goto(-300, 350) #Go to the top left corner of the screen 
    color("white") #Make the pen white
    fillcolor("white") #Fill the shape with white
    begin_fill() #Start filling the shape
    circle(50) #Make a circle of radius 50
    end_fill() #Stop filling the shape
    hideturtle() #Hide the pen


overallcoords = [] #Keep the coordinates of the stars in a list so we can make sure that the stars don't overlap
for i in range(25):
    penup() #Raise the pen when moving to new coordinates if you don't want to draw
    x = random.randint(-300,300)
    y = random.randint(-300,300) 
    currentcoords = [x,y] #Save the coordinates of the star in a list
    goto(currentcoords[0], currentcoords[1]) #Go to a random position on the screen
    
    right(random.randint(0,360)) #Rotate the pen to a random angle
    pendown() #Lower the pen
    makeStar() #Make a star
    penup() #Raise the pen 

makeMoon() #Make the moon

done() #End the program
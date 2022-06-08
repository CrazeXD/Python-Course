#There are many different modules available to make GUIs in Python

#Inbuilt in python is the Tkinter library

#I generally am not a huge fan of tkinter, however, I will show how to make simple GUIs with this module

from logging import RootLogger
from re import T
from tkinter import *

root = Tk() #Initialize the class

root.title("A Totally Useful GUI") #Set the name of the window

root.geometry("300x500") #Set the window size WIDTHxHEIGHT

lbl = Label(root, text = "Tkinter GUIs Don't Look Very Good")
#We can configure this button from outside the class as well
lbl.configure(activeforeground = "red")
#We can also use the [] brackets
lbl["font"] = "Cambria 14" #Font Name Size

#There are many ways to add the label onto the GUI
#The 2 main ones are .pack(side = "") or .grid(x, y)
lbl.grid()

#There are lots of other widgets that we can use

button = Button(root, text = "Click me!")
#We can set a command that happens when the button is pressed
def clicked():
    button.configure(text = "I have been clicked!")
button.configure(command = clicked)
button.grid() #We can't use 2 different types of packs

#We can also have a text entry system

myText = Entry(root, width = 20, text = "Default text")
myText.grid()

#To get what is inside of the text, we can use .get()
def getText():
    res = "You wrote " + myText.get()
    lbl.configure(text = res)

button2 = Button(root, text = "What is in your text?", command = getText)
button2.grid()

#To add a menu bar we can use the Menu class
menu = Menu(root)
item = Menu(menu)
item.add_command(label = "New")
menu.add_cascade(label = "File", menu = item)
root.config(menu = menu)


#We can also give the user prompts, using the messagebox package

from tkinter import messagebox

def message(): 
    a = messagebox.askyesno("Messagebox", "Do you like this class so far?") #This is one of many prompts provided by the messagebox library
    print(a)
button3 = Button(root, text = "Send me a prompt", command = message)
button3.grid()
root.mainloop() #Start the GUI

#To close the application, we can call .destroy() on the root object

import time

time.sleep(30)

root.destroy()
from tkinter import *

window = Tk()

window.title("A Totally Useful GUI") #Title the window

window.geometry("1080x720") #Set the size of the window width WIDTHxHEIGHT

#To add "widgets" to the GUI, we have to store them as variables

#Let's start with a label

myLabel = Label(window)
#There are multiple ways to configure this label
#The first is to set the configurations when calling it
myLabel = Label(window, text = "Hi!", activebackground = "blue", activeforeground = "green")
#We can also use .config
myLabel.config(activebackground = "light grey", activeforeground="red")

#Finally, we can do it using [] brackets


#There are mutliple ways to add this button to the GUI, however, let's start with the simplest

myLabel.pack()

#We can change where it is packed using an argument
myLabel.pack(side = "left")

window.mainloop()
#In this class we will be doing some challenge questions in python that will help you with both algorithms and python in general
#However, I just want to quickly teach you all 2 small concepts.
#First, the exit() command. 
#To exit a python program, simply call exit() anywhere in your code.
#Secondly, dictionaries.
#Dictionaries can be used to link 2 different values.

myDict = {"John": "A", "Sam": "B"}
#To access a certain members data:
print(myDict["John"])
#We can access parts of dictionaries by index as well
print(myDict[0])
#To change the value of an item
myDict["Sam"] = "C"
myDict.update("Sam": "A")
#We can find the length of a dictionary using len()
print(len(myDict))
#To add items to a dictionary
myDict["NewName"] = "D"
myDict.update("NewPerson": "C"}
#We can remove items by popping them out
myDict.pop("NewName")
#.popitem() removes the last added item
myDict.popitem()
#You can also use the del keyword
del myDict["John"]
del myDict #Deletes the varaible so we can't print it
#To simply clear the dictionary, we can use .clear()
songs = {"Hello": "Adelle", "Faded": "Alan Walker", "Whenever, Wherever": "Shakira"}
songs.clear()
#We can put dictionaries inside of dictionaries as well
#We can also loop through dictionaries
for i in songs:
	print(i) #Prints dictionary name
	print(songs[i]) #Prints dictionary value

#Now for some challenges!!!


#Challenge 1: Given a list of people, return a list of the lengths of their names
#Challenge 2: Using the OS module, walk through a big folder anywhere on your computer. If the file is a .txt(check with the .endswith() function), print the contents of that file.
#Note: You may put the python file in the folder that you are navigating.

#Challenge 3: Make a clock app using the time module and Tkinter.
#Challenge 4: Given 2 files, one of usernames, and one of passwords, ask a user to login. If their username matches their password, print that they have succesfully logged in.
#Otherwise, tell them that they have entered an incorrect login.

#In this class we will be doing some challenge questions in python that will help you with both algorithms and python in general
#However, I just want to quickly teach you all a small concept.
#First, the exit() command. 
#To exit a python program, simply call exit() anywhere in your code.

#Now for some challenges!!!


#Challenge 1: Given a list of people, return a list of the lengths of their names
#Challenge 2: Using the OS module, walk through a big folder anywhere on your computer. If the file is a .txt(check with the .endswith() function), print the contents of that file.
#Note: You may put the python file in the folder that you are navigating.

#Challenge 3: Given 2 files, one of usernames, and one of passwords, ask a user to login. If their username matches their password, print that they have succesfully logged in.
#Otherwise, tell them that they have entered an incorrect login. 
#Once logged in, make a file for the user. If one already exists, open this.
#In this file, on the first line, write the username that they entered.
#On the second line, write down the current date and time. Replace this line if they relogin.
#On the third line, write how much funds they have in their account. If they have none, write 0. Make functions to change this value, as well as view it.


#Challenge 4: Design a class that represents a phone. The phone should have a number, a storage capacity, and a battery life.
#In the phone, the following functions should be implemented:
    #1. __init__(self, number, storage, battery)         #Initialize the phone
    #2. getBatteryLife(self) -> int                       #Gets the battery life
    #3. downloadApp(self, appSize)                       #Downloads an app from the internet. Only works if the storage capacity is greater than the app size+current storage used. There also must be battery in the phone.
    #The download will take the appSize from the storage capacity. It will also reduce battery by 3% for each app downloaded.
    #4. getStorage(self) -> int                          #Gets the current storage capacity
    #5. getNumber(self) -> str                           #Gets the phone number
    #6. usePhone(self, minutes) -> None                  #Uses the phone for minutes. This will reduce the battery by 1% for each minute used
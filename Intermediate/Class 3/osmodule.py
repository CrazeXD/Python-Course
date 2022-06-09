#In this tutorial, we will learn to use the os module to work with the operating system and the file system.

import os

print(os.getcwd()) #Get the current working directory (the directory you are in)

print(os.listdir()) #List the files in the current working directory

os.system("") #This function takes any command and runs it in the terminal

print(os.cpu_count()) #Get the number of CPUs (cores) on your computer

os.mkdir("TestFolder") #Create a new folder

os.rename("TestFolder", "TestFolder2") #Rename a folder

os.rmdir("TestFolder2") #Delete a folder

for i in os.walk(os.getcwd()):
    print(i)
    
print(os.getlogin()) #Get the current user's login name

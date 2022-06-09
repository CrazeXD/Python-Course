# Strings are values that contain text
# They can be placed either in a variable or as an argument in a function

# Strings can have any charchter in them, however some require an extra step

#The following features can be used in strings to make them more versatile

newline = '\n'
quotes = '\' or \"'
print(newline, quotes)
#To ignore the \ charachter as a key, use a double \

noslash = "C:\\users\\"
print(noslash)
# Triple quotes can also be used in variables to add multiple lines

multiline = '''
Hi
Hello
Welcome
Hola
'''
print(multiline)
#If you want to put a variable in a string, you can do one of the following methods

#A f string can be used, and you put the variable in the {} brackets

name = "John"
compname = "Alexa"
print(f"Hello {name}, my name is {compname}.")

#Another option is a .format()
#Write the variables in order they appear in the string
print("Hello {}, my name is {}.".format(name, compname))

#To make a string completely lower case or uper case, you can use the .lower or .upper function

multiline = multiline.lower()
print(multiline)
multiline = multiline.upper()
print(multiline)

#To find the length of a string, use the len() function
thing = "Hello"
print(len(thing))

#In a string, each charachter has a number associated with it
#This number is caled an indice
#Indices start at 0, and go up to the length of the string - 1
#For example, in the string "Hello", the first charachter is at index 0, the second at index 1, and so on
#We can get the charachter at a specific index by using the [ ] brackets

indiceofh = thing[0]
print(indiceofh)
#To get the last charachter in a string, use the [-1] brackets
indiceoflast = thing[-1]
print(indiceoflast)
#To get the indice of a charachter or a substring in a string, use the .index() function
#The .index() function returns the indice of the first instance of the substring
#If the substring is not found, it will throw an error
print(thing.index("He"))
#If we want to print the indice of the last instance of the substring, we can use the .rindex() function
print(thing.index("l"))

#We can iterate through each charachter in a string using a for loop or a while loop, which we will learn about later

#To add 2 strings together, we can concatenate or add them
string1 = "Hello"
string2 = "World"

resultwithadd = string1+string2
print(resultwithadd)

#There are many other features, however, these are some of the most important that you will use
#If you would like a list, just google "Python String Functions"
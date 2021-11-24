# Strings are values that contain text
# They can be placed either in a variable or as an argument in a function

# Strings can have any charchter in them, however some require an extra step

#The following features can be used in strings to make them more versatile

from typing import MutableMapping


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

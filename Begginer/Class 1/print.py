print("Hello World")

#Each print statement makes a new line in the console

#We can add multiple strings to the print statement using a , in between each string

print("Hi", "Hello", "Welcome", "Hola")

#We can also add variables to the print statement, which we will learn about in the next section
#We can also seperate these strings with whatever we want
#By default, python uses a space to seperate strings however we can change that to any other character or string
#We can also change the seperator to be empty, which will make the strings appear on the same line without a space in between
print("Hello", "World", sep=", ")

#We can also add a custom charachter after each print statement, so instead of making a new line it creates a comma, for example

print("Hello", end = ", ")
print("World")
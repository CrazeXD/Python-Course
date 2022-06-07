#Functions are a series of instructions that can be reused in your code
#In python, a function can be defined in the following way

def myFunction():
	#Do something
	print("This is a function!")

#We then have to call the function

myFunction() #make sure to have the () whenever calling a function

#A function can take different arguments, which are basically pieces of data that the function can use

def add(n1, n2):
	print(n1+n2)

add(3, 4)
#Instead of just printing the function, we can use a statement called return to get some value out of the function

def subtract(n1, n2):
	return n1-n2

subtracted = subtract(5, 6)
print(subtracted)

#Challenge! Make a function that takes a string in as an argument. Then, ask the user whether they would like to make it upper case or lower case, and convert and return the string
#appropriately

def upperLower(strings):
	choice = input("Would you like to convert the string to uppercase or lowercase?\n")
	if choice.lower() == "uppercase":
		return strings.upper()
	elif choice.lower() == "lowercase":
		return strings.lower()
	else:
		return strings

print(upperLower("hElLo"))
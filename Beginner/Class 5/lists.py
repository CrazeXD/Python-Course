fruits = ["apples", "oranges", "bannanas", "peaches", "mangoes", "papayas", "grapes"]
#This is a list
#A list is a collection of data that is ordered and can be changed
#A list can have any kind of data type stored in it
#A list can be created by using square brackets
#Like a string, each value in a list has a number associated with it called an index

print(fruits[0])

#To get the index of a certain value in a list, use the .index() function

print(fruits.index("oranges"))

#We can also iterate through the elements in a list using a for loop
for i in fruits:
    print(i)

#Lists can contain any data type

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    print(i)

#We can even store lists inside of lists, which are called nested lists
lists = [[3, 5], [1, 3], [2, 4], [5, 7]]
#To access the elements of a 2D list, use multiple pairs of [] brackets
print(lists[1][0]) #This will print 1

#To add a value to a list, use the .append() function
numbers.append(11)
print(numbers)
#To remove a value from a list, use the .remove() function
numbers.remove(11)
print(numbers)

#Next, we can use dictionaries
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

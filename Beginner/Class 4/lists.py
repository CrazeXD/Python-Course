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
#To remove a value from a list, use the .remove() or the .pop() function. The .pop() function removes the last element in the list if no value is passed
#Pop takes an index as an argument and returns the value it removes
numbers.remove(11)
print(numbers)
print(numbers.pop(8)) #Removes and prints the value at index 8

#We can reverse lists
numbers.reverse()
print(numbers)
#We can order lists in increasing or decreasing order
numbers.sort()
numbers.sort(reverse=True)
print(numbers)

#To add 2 lists, we can use the .extend() function
names = ["John", "Jane", "Mary", "Bob"]
names2 = ["Tom", "Tim", "Timmy", "Timothy"]
names.extend(names2)
print(names)

#We can get the # of times a value appears in a list using the .count() function
names.extend("Tim")
print(names.count("Tim"))


#Next, we can use dictionaries
#Dictionaries can be used to link 2 different values.

myDict = {"John": "A", "Sam": "B"}
#To access a certain members data:
print(myDict["John"])
#To change the value of an item
myDict["Sam"] = "C"
myDict.update({"Sam": "A"})
#We can find the length of a dictionary using len()
print(len(myDict))
#To add items to a dictionary
myDict["NewName"] = "D"
myDict.update({"NewPerson": "C"})
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

#To get a list of all the keys in a dictionary, we can use the .keys() function
songs = {"Hello": "Adelle", "Faded": "Alan Walker", "Whenever, Wherever": "Shakira"}
listkeys = list(songs.keys())
#To get a list of all the values in a dictionary, we can use the .values() function
listvalues = list(songs.values())
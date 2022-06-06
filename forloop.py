# For loop
# Python has another kind of loop called a for loop, which allows you to go through every value in a certain value

a = "Hi"
b = 7
for i in a:
    print(i)



for i in range(b):
    print(i)


#Observer what number the second loop prints up to
#Since python starts from 0, it doesn't include the last value
#In order to use the last value with the range() function, you can use the following

for i in range(b+1):
    print(i)



#In this way, we go up to the max value
#If we don't want to start from 0, we can change the minimum value

for i in range(3, b+1):
    print(i)



#In order to increase by a certain increment, use a third argument

for i in range(1, b+1, 2):
    print(i)


#This code increments by 2 every time

#Nested Loops

#You can have a loop inside of another loop

for i in range(6):
    for g in range(11):
        print(i*g)

#This code will create a multiplication table, printing every value from 0*0 to 5*19

#We can iterate through a string using a for loop, like I mentioned earlier

string = "Python is fun!"
for i in a:
    print(i)

#Or we can do it by indice
stringlength = len(string)
for i in range(stringlength-1):
    print(string[i])

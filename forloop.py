# For loop
# Python has another kind of loop called a for loop, which allows you to go through every value in a certain value

a = "Hi"
b = 7
for i in a:
    print(i)

print('--------------------------------------------')

for i in range(b):
    print(i)

print('--------------------------------------------')
#Observer what number the second loop prints up to
#Since python starts from 0, it doesn't include the last value
#In order to use the last value with the range() function, you can use the following

for i in range(b+1):
    print(i)

print('--------------------------------------------')

#In this way, we go up to the max value
#If we don't want to start from 0, we can change the minimum value

for i in range(3, b+1):
    print(i)

print('--------------------------------------------')

#In order to increase by a certain increment, use a third argument

for i in range(1, b+1, 2):
    print(i)

print('--------------------------------------------')
#This code increments by 2 every time
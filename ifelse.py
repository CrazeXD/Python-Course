#In python, we can check if a certain condition is true
#When making conditions, we use the comparison features we learned earler

a = 3
b = 5

if a == b:
    print("Yes!")
else:
    print("No!")

'''
If we want to have multiple if statements but only execute 1 of the statements, we can use elif
The difference between running multiple if state ments and an elif statement is that an elif statement
only does the first condition that is true, while an if statement does all of the statements that are true
'''

if a == 3:
    print("True! a = 3")

if b == 5:
    print("True! b = 5")

print("Verus")

if a == 3:
    print("True! a = 3")
elif b == 5:
    print("True! b = 5")

#In the second example, only the first one is printed, while in the first example, both are done
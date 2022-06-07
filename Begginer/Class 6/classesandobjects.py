#Classes and Objects

#Classes are blueprints for creating objects
#Classes contain values and functions, which can be reused
#Classes are defined using the keyword class
#They are used to keep code organized, as well as keep track of different functions and values


#Note: The pass keyword is a placeholder. It tells Python to do nothing.
#This is often used as a placeholder when defining a class, as a way to get around having to define the __init__() function, which is a required function for any class
#The __init__() function is a special function that is called when you create a new object from that class
#It automatically executes when you create a new object for that class, and it stands for initialize.

class myClass:
    def __init__(self, value):
        self.value = value 
        #The self keyword is a reference to the current instance of the class, and is used to access variables that belong to the class
        #All functions in a class require self as the first argument, unless you define them with special keywords such as @classmethod and @staticmethod (these are described
        #in more advanced courses)
        print("myClass initialized")
        print(f"You're value is {self.value}")
    
    def add(self, x, y):
        return x+y
    def subtract(self, x, y):
        return x-y
    def multiply(self, x, y):
        return x*y
    def divide(self, x, y):
        return x/y
    

#To create an object, we need to call the class in a variable
object = myClass(5) #This creates an object of the class myClass, and stores it in the variable object
#Inside the parenthesis, we need to pass any values that the __init__ function requires (besides self)
#We can now perform any operations on the object that are defined in the class
#To do this, we need to call the function inside the object by writing objectname.functionname(arguments) and putting that in a print statement
print(object.add(5,6))
print(object.subtract(5,6))
#And we can do this for all the functions in the class
#We can also create multiple objects of the same class
object2 = myClass(10)
print(object2.multiply(5,6))

#Challenge: Create a class called Students, which has the functions addGrade, removeGrade, and averageGrade
#The addGrade function should add a grade to the list of grades, which is stored as a variable in the object (self.variable)
#The removeGrade should remove a grade from the list of grades, which is stored as a variable in the object (self.variable)
#The averageGrade should return the average of the grades in the list of grades, which is stored as a variable in the object (self.variable)
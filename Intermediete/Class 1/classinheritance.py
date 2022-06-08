#In python, we have the option to make classes that inherit properties from another class


class Parent:
	def __init__(self, name, age) -> None:
		self.name = name
		self.age = age

	def printer(self) -> None:
		print(f"{self.name} is {self.age} years old.")

class Child(Parent):
	pass

#Even though the Child class has no features on it's own, we can still access data from Parent
child = Child("Rishabh", 14)
child.printer()

#We can also add even more data to the new class

class Student(Child):
	#If we want an __init__ function in this class, but we also want to use __init__ from the parent class, we have to first call the Parent class
	#However, the arguments that the child __init__ function takes must include all of the ones from parent as well
	def __init__(self, name, age, school):
		self.school = school
		Parent.__init__(self, name, age)
	def getGraduationYear(self) -> None: #The -> indicates what type of value the function will return. It is not neccesary to add.
		yearstillgraduation = 18-self.age
		if yearstillgraduation>0:
			print(f"{self.name} has {yearstillgraduation} years until they graduate")


student = Student("Rishabh", 14, "Wonderful High School")
student.getGraduationYear()

#Practice: Make a code that has a parent class rectangle and a child class square.
#The parent class should have functions area and perimeter
#The child class should be able to use those functions
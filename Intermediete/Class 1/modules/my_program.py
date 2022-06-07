#Import your modules
#If you want to make a module, or store functions/classes in another file, we can use the import statement.
#For example, make a new folder called modules and create a file called my_module.py.
#In that module, make a function called hello_world() that prints "Hello World!"
#Now make another file in that folder called my_program.py.
#In that file, import the module my_module.py and call the function hello_world()

import my_module
my_module.hello_world()

#We can also make modules availaible to all codes by adding it to the import directory, but that is much more complicated for now.

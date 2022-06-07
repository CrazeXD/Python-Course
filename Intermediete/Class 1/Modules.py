#Modules
#Python provides a great way to use modules. Modules are just python files that contain functions and classes.
#These modules are imported into your program and you can use them by simply calling the name of the module.
#To import a module, simply use the import keyword and the name of the module.
import time
#The time module is an inbuilt module with python. It provides functions to work with time and dates, as well as lets your 
#program sleep (or stop doing anything) for a certain time period

#To import certain parts of a module, we can use the from keyword.

from time import time, sleep

#If we use the from keyword, we don't have to specify the name of the module when calling the function.

print(time()) #Prints the current time
sleep(6) #Sleeps for 6 seconds

#We can also import all the functions from a module.
from time import *
#Almost all the modules you will use will have documentation available online. To get this documentation, just run a general google search.

#Some modules will also have a help() function.
#To see what a function does, just call help(function_name).
#You must have the module imported however
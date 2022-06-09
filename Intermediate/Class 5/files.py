#Files are an important part of any program.
#Files can be used to store data, access data, and manipulate data.
#Let's start with opening a file.

testfile = open("test.txt", "r")
#The second argument is the mode.
#There are many different modes in python.
#The "r" means read.
#The "w" means write. The file will be created if it does not exist.
#The "a" means append.
#The "r+" means read and write.
#The "w+" means write and read. 
#The "a+" means append and read.
#The "b" means binary.
#If we add "b" to the end of the mode, we can read and write binary files.
#For example, "wb" means write binary.
#Let's test this out
#For now, let's stick with reading.
#To access the contents of the testfile, we can use the read() method
text = testfile.read()
print(text)
testfile.close() #ALWAYS CLOSE YOUR FILES!


#Now, let's take a look at some write functions
#The write() method writes to the file.
testfile = open("test.txt", "w")
testfile.write("This is a test")
testfile.close()
#Now let's read the file again.
testfile = open("test.txt", "r")
text = testfile.read()
print(text)
testfile.close()
#And wala

#For the remainder of the class, I want you all to build a small program that will allow you to create a file.
#The program should ask the user for a filename, and then ask for the contents of the file.
#As an optional additional practice, you can make this applicaiton into a GUI using tkinter.
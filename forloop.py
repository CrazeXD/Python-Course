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
#If we don't want to start from 0, we can change the minimum valueecho "# Python-Course" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/CrazeXD/Python-Course.git
git push -u origin main
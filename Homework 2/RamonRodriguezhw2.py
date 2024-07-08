'''***************************************
* Homework 2: Lesson 2: For Loops
* Student: Ramon Rodriguez-Hernandez
* Date: July 5, 2024
******************************************'''

'''Problem 1: program that prints your name 100 times.'''
for i in range(100):
    print('Ramon Rodriguez-Hernandez')


'''Print statement to seperate statements in terminal'''
print(' ')


'''Problem 2: program that uses a for loop to print the numbers 100, 98, 96, ... , 4, 2.'''
for i in range(100, 0, -2):
    if i == 2:
        print(i)
    else:
        print(i, end = ',')


'''Print statement to seperate statements in terminal'''
print(' ')



'''Problem 3: program that uses exactly four for loops to print the sequence 
"AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG":'''
for a in range(10):
    print('A', end = '')

for b in range(7):
    print('B', end = '')

for cd in range(4):
    print('CD', end = '')

for effffffg in range(1):
    print('EFFFFFFG', end = '')


'''Print statement to seperate statements in terminal'''
print(' ')
'''Print statement to seperate statements in terminal'''
print(' ')


'''Problem 4: program that asks the user for their name and how many times to print it. The program
should print out the user's name the specified number of times.'''
name = input('Enter your name: ' )
count = eval(input('Enter how many times you would like to print your name: '))
for i in range(count):
    print(name)


'''Print statement to seperate statements in terminal'''
print(' ')


'''Problem 5: Use a for loop to print a box like the one below. Allow the user to specify how wide 
and how high the box should be. [Hint: print('*'*10) prints ten asterisks.].'''
width = eval(input("Enter how wide: "))
height = eval(input('Enter how high: '))

for i in range(height):
    print('*' * width)


'''Print statement to seperate statements in terminal'''
print(' ')


'''Problem 6: Use a for loop to print a triangle like the one below. Allow the user to specify how 
high the triangle should be.'''
heightTriangle = eval(input('Enter how high the triangle should be: '))
for i in range(heightTriangle):
    print ('*'*(i+1))


'''Print statement to seperate statements in terminal'''
print(' ')


'''Problem 7: Use for loops to print a diamond like the one below. Allow the user to specify how 
high the diamond should be.'''
heightDiamond = eval(input('Enter the height of the diamond: '))
for i in range(1, heightDiamond // 2 + 2):
    print(' ' * (heightDiamond // 2 + 1 - i) + '*' * (2 * i - 1))


for i in range(heightDiamond // 2, 0, -1):
    print(' ' * (heightDiamond // 2 + 1 - i) + '*' * (2 * i - 1))
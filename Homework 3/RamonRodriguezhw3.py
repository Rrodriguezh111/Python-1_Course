'''***************************************
* Homework 3: Lesson 3: Numbers
* Student: Ramon Rodriguez-Hernandez
* Date: July 5, 2024
******************************************'''
from random import randint
from random import uniform
import math

'''Problem 1: Write a program that generates a random number between 1 
and 10 and prints your name that many times.'''
x = randint(1, 10)

for i in range(x):
    print('Ramon Rodriguez-Hernandez')


'''Print statement to seperate statements in terminal'''
print(' ')


'''Problem 2: Write a program that generates a random decimal number 
between 1 and 10 with two decimal places of accuracy. Examples are 
1.23, 3.45, 9.80, and 5.00.'''
random = round(uniform(1.00, 10.00), 2)
print('Random number is ', random)


'''Print statement to seperate statements in terminal'''
print(' ')


'''Problem 3: Write a program that asks the user for a number of seconds 
and prints out how many minutes and seconds that is. For instance, 
200 seconds is 3 minutes and 20 seconds. [Hint: Use the //
operator to get minutes and the % operator to get seconds.]'''
seconds = eval(input('Enter the number of seconds: '))
minutes = seconds // 60
secondsremaining = seconds % 60

print(seconds, 'seconds is ', minutes, 'minutes and ', secondsremaining, 'seconds')


'''Print statement to seperate statements in terminal'''
print(' ')


'''Problem 4: Write a program that asks the user for an hour between 1 
and 12 and for how many hours in the future they want to go. Print out 
what the hour will be that many hours into the future.'''
currenthour = eval(input('Enter hour (1-12): '))
hoursahead = eval(input('How many hours ahead?: '))

newhour = (currenthour + hoursahead) % 12

if newhour == 0:
    newhour = 12

print('New hour: ', newhour, 'o\'clock')


'''Print statement to seperate statements in terminal'''
print(' ')


'''Problem 5.A: One way to find out the last digit of a number is to mod 
the number by 10. Write a program that asks the user to enter a power. 
Then find the last digit of 2 raised to that power.'''
power = eval(input('Enter a power: '))
result = 2 ** power

lastdigit = result % 10

print('The last digit of 2^', power, 'is ', lastdigit)


'''Print statement to seperate statements in terminal'''
print(' ')


'''Problem 5.B: One way to find out the last two digits of a number is 
to mod the number by 100. Write a program that asks the user to enter 
a power. Then find the last two digits of 2 raised to that power.'''
power2 = eval(input('Enter a power: '))
result2 = 2 ** power2

last2digits = result2 % 100

print('The last digit of 2^', power2, 'is ', last2digits)


'''Print statement to seperate statements in terminal'''
print(' ')


'''Problem 5.C: Write a program that asks the user to enter a power 
and how many digits they want. Find the last that many digits of 2 
raised to the power the user entered.'''
power3 = eval(input('Enter a power: '))
numdigits = eval(input('Enter the number of: '))
result3 = 2 ** power3

modulus = 10 ** numdigits

lastdigits = result3 % modulus

print('The last digit of ', numdigits, '^', power3, 'is ', lastdigits)



'''Print statement to seperate statements in terminal'''
print(' ')



'''Problem 6: Write a program that asks the user to enter a weight 
in kilograms. The program should convert it to pounds, printing the 
answer rounded to the nearest tenth of a pound.'''
kilograms = eval(input('Enter weight in kilograms: '))
conversionfactor = 2.20462

pounds = kilograms * conversionfactor

poundsrounded = round(pounds, 1)

print(kilograms, 'kilograms is approximately ', poundsrounded, 'pounds')


'''Print statement to seperate statements in terminal'''
print(' ')


'''Problem 7: Write a program that asks the user for a number 
and then prints out the sine, cosine, and tangent of that number.'''
number = eval(input('Enter a number: '))

sinevalue = math.sin(number)
cosinevalue = math.cos(number)
tangetvalue = math.tan(number)

print('Sine of',number,'\b:', sinevalue)
print('Cosine of',number,'\b:', cosinevalue)
print('Tanget of', number, '\b:', tangetvalue)


'''Print statement to seperate statements in terminal'''
print(' ')


'''Problem 8: Write a program that draws “modular rectangles” like 
the ones below. The user specifies the width and height of the rectangle,
 and the entries start at 0 and increase typewriter fashion from left to 
 right and top to bottom, but are all done mod 10. Below are examples of 
 a 3 × 5 rectangle and a 4 × 8.'''
width = eval(input('Enter the width of the rectangle: '))
height = eval(input('Enter the height of the rectangle: '))

for i in range(height):
    for j in range(width):
        print((i * width + j) % 10, end=' ')
    print()

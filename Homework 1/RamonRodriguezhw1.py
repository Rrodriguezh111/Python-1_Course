'''***************************************
* Homework 1: Lecture 1: Introduction
* Student: Ramon Rodriguez-Hernandez
* Date: July 2, 2024
******************************************'''


'''#1.A Following loop statement prints the following:
******************
*                *
*                *
******************
'''
for i in range(4):
    if i == 0 or i == 4 - 1:
        print('*' * 18)
    else:
        print('*' + ' ' * (18 - 2) + '*')


'''Print statement to seperate statements in terminal'''
print(' ')


'''#1.B Following loop statement prints the following:
*
**
***
****
'''
for i in range(4):
    print ('*'*(i+1))


'''Print statement to seperate statements in terminal'''
print(' ')


'''#1.C  program that computes and prints the result of (512-282)/(47x48+5), 
It is roughly 0.1017'''
numerator = (512 - 282)
denominator = (47 * 48 + 5)
result = numerator / denominator

print(result)


'''Print statement to seperate statements in terminal'''
print(' ')


'''#2 Input: Ask the user to enter a number x. Use the sep optional argument to print out x, 2x, 3x,
4x, and 5x, each separated by three dashes'''
x = eval(input("Enter a number: "))
print(x, 2*x, 3*x, 4*x, 5*x, sep='---')


'''Print statement to seperate statements in terminal'''
print(' ')


'''#3.A program that asks the user for a weight in kilograms and converts it to pounds'''
ConversionScale = 2.2

kilograms = eval(input('Enter weight in kilograms: '))
conversion = kilograms * ConversionScale
print(kilograms, ' Kilograms is equal to ', conversion, ' pounds. ')


'''Print statement to seperate statements in terminal'''
print(' ')


'''#3.B  Ask the user for the price of the meal and the
percent tip they want to leave. Then print both the tip amount and the total bill with the tip included'''
MealPrice = eval(input('Enter the price of the meal: $'))
TipPercentage = eval(input('Enter the percentage tip: %'))
 
TipAmount = MealPrice * (TipPercentage / 100)
TotalBill = MealPrice + TipAmount

print('Tip Amount: ', TipAmount)
print('Total bill including tip: $', TotalBill)
#import random 	#random num generator
#import sys	#sys module 
#import os	#OS module

#'''
#Basics

#'''

#print("Hello World")

name = "Edson de Aguiar"
age = 20

print(name)
print(age)

'''
Operations
PEMDAS matters

'''
print("5 + 7 = ", 5+7)
print("5 - 7 = ", 5-7)
print("5 * 2 = ", 5*2)
print("5 / 2 = ", 5/2)
print("5 % 2 = ", 5%2)
print("5 ** 2 = ", 5**2)
print("5 // 2 = ", 5//2)

'''
Strings

'''
quote = "\"First String"
multi_line_quote = '''Second String'''

final_String = quote + multi_line_quote

print(final_String)
print("%s %s %s" %('Testing: ', quote, multi_line_quote))

print("--------Printing X amount of new lines--------")
print('\n' * 6)
print("--------Printing without new line--------")
print("Remove new line", end="")
print("No new line")
print(" New Line removal is gone")



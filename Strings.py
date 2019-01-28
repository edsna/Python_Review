import random 	#random num generator
import sys	#sys module 
import os	#OS module

'''
More on Strings

'''

LargeStr = "THis is a relatively very long string"

print(LargeStr[0:7])

#The 5 char
print(LargeStr[-4])
print('\n')
#All untill the 5th char
print(LargeStr[:-5])
print('\n')
print(LargeStr[:7] + "Added string")

print("%c is my %s letter and my number %d is %.5f" %('A', 'Favorite', 1, .14))

#capitalize first letter of string
print(LargeStr.capitalize())

#Finding index value of string
print(LargeStr.find("Tip"))

#ret true of input is all strings
print(LargeStr.isalpha())

#ret true of input is all ints
print(LargeStr.isalnum())

#ret length of string
print(len(LargeStr))

#Replace first str with second
print(LargeStr.replace("Tip", "Top"))

test = "a manha"
print(test)
#Strip white space
print(test.strip())








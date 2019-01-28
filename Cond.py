import random 	#random num generator
import sys	#sys module 
import os	#OS module

'''
Conditionals >> Execute code if cond is met

'''
age = 21

if age > 16 :
	print("You are old enough to drive")
else : 
	print("You are not old enough to drive")


if age >= 21 :
	print("You are old enough to drive a truck")
elif age >= 16 : 
	print("You are old enough to drive a car")
else :
	print("You are not old enough to drive")

print("-----------COnditional Operators--------------")

if((age >= 1) and (age <= 18)):
	print("Its your birthday")
elif(age == 21) or (age >= 65):	
	print("Its your birthday")
elif not(age == 30):	#not > negates condition to its right
	print("You don't have a birthday")
else:
	print("Your party")

import random 	#random num generator
import sys	#sys module 
import os	#OS module

'''
Loops

'''
for x in range(0,10):
	print(x, ' ', end="")

print('\n')

cars = ['BMW', 'Ferrari', 'VW']

for y in cars:
	print(y,)
for x in [2,4,6,8,10]:
	print(x)
test = [[1,2,3],[10,20,30],[100,200,300]]
for x in range(0,3):
	for y in range(0,3):
		print(test[x][y])

ran = random.randrange(0,100)

while(ran != 20):
	print(ran)
	ran = random.randrange(0,100)

i = 0;

while(i <= 20):
	if(i%2 == 0):
		print(i)
	elif(i == 9):
		break
	else:
		i += 1
		continue

import random 	#random num generator
import sys	#sys module 
import os	#OS module

'''
Dictionaries >> stores unique values and one cannot join dictionaries
They're stored as Key > Value 

'''

port = {'Mae' : 'Mom',
	'Pai' : 'Dad',
	'Pao' : 'Bread',
	'Carro' : 'Car',
	'Viola' : 'Guitar',
	'Pasta' : 'Bag'}

print(port['Carro'])
del port['Pao']
port['Pasta'] = 'Backpack'
print(port['Pasta'])
print(len(port))
print(port.get("Mae"))
print(port.keys())
print(port.values())



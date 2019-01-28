import random 	#random num generator
import sys	#sys module 
import os	#OS module

'''
I/O

'''

myFile = open("test.txt", "wb")


print(myFile.mode)
print(myFile.name)
myFile.write(bytes("Write this to the file\n", 'UTF-8'))

myFile.close()

myFile = open("test.txt", "r+")

mF = myFile.read()
print(mF)

#Deletes file
#os.remove("myFile.txt")

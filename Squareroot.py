#Katylub, exercise 7
#Write a program that that takes a positive floating point number as input and outputs
# an approximation of its square root.

#Enter a positive floating point number ( I did research how in tutorial)
n = float(input("Input a positive floating point number: "))

#I did research in page www.geeksforgeeks.org
import math 
print ('The square root of', n, 'is approx.', (math.sqrt(n)))
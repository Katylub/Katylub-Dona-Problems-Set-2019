# Katylub, exercise 6
# Write a program that takes a user input string and outputs every second word.

#User need to enter a string
s = str(input("Input a string: "))
#Create a list first and make sure read every second word
l= s.split () [::2]
# Eliminate list format 
l=" ".join (l)
print (l)

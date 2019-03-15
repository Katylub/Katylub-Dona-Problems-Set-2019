#Exercise 9 - Katylub Dona
#Write a program that reads in a text file and outputs every second line. The program
#should take the filename from an argument on the command line.


# Research how to take the file name from an argument https://stackoverflow.com
import sys

f = open("sys.argv[0]","r")
contents = f.read()
f.close()
print contents
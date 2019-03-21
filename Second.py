#Exercise 9 - Katylub Dona
#Write a program that reads in a text file and outputs every second line. The program
#should take the filename from an argument on the command line.


# Tried several times and took as main referal https://stackoverflow.com 

#Take the filename from an argument on the command line and is represented as Title. I took the second file as Title for the name
import sys
print ("Title:", (sys.argv[1]))

# Reads file Example.txt and output every second line
with open('example.txt', 'r') as f:
    count = 0
    for line in f:
        count+=1
        if count % 2 == 0: #this is the remainder operator
            print(line)
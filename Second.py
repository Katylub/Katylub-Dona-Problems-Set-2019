#Exercise 9 - Katylub Dona
#Write a program that reads in a text file and outputs every second line. The program
#should take the filename from an argument on the command line.


# Tried several times and took as a referal https://stackoverflow.com


with open('example.txt', 'r') as f:
    count = 0
    for line in f:
        count+=1
        if count % 2 == 0: #this is the remainder operator
            print(line)
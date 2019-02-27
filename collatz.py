# Katylub, exercise 4
# Asks the user to input any positive integer and outputs the
#successive values of the following calculation. At each step calculate the next value
#by taking the current value and, if it is even, divide it by two, but if it is odd, multiply
#it by three and add one. Have the program end if the current value is one.

#Use a positive number
n = int(input("Input a positive number: "))

x = 0
 
for x in range(1, n):
    if(n % 2 == 0):
        x = x/2
    else:
        x=(x*3)/2
 
print(n)


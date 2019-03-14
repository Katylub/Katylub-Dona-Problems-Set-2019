# Katylub, exercise 4
# Asks the user to input any positive integer and outputs the
#successive values of the following calculation. At each step calculate the next value
#by taking the current value and, if it is even, divide it by two, but if it is odd, multiply
#it by three and add one. Have the program end if the current value is one.

#After several trials and research I took as reference https://python-forum.io
  
#Define the function
def collatz(number):
    #If is even
    if number % 2 == 0:
        return number//2
        #If is odd
    else:    
        result = 3*number + 1
        return result       
try:
    #Add the value
    n = int(input("Please enter a positive number: "))
    while n != 1:
        print (n)
        n = collatz(abs(n))
except ValueError:
    print('Type a number please!')
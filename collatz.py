# Katylub, exercise 4
# Asks the user to input any positive integer and outputs the
#successive values of the following calculation. At each step calculate the next value
#by taking the current value and, if it is even, divide it by two, but if it is odd, multiply
#it by three and add one. Have the program end if the current value is one.

#I did it taking many websites as reference
  
num = int(input("Please enter a positive integer: "))

def collatz(num):
    while num != 1:
        print(num)
        if num % 2 == 0:
            num = int(num / 2)
        else:
            num = int(3 * num + 1)
    else:
        print(num)
       
print(collatz(num))
        

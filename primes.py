# Katylub, exercise 5
# Write a program that asks the user to input a positive integer and tells the user
# whether or not the number is a prime.

#Enter a positive number
number = int(input("Input a positive number: "))

#A number is said to be prime if it is only divisible by 1 and itself
#After I tried, I took as reference: https://beginnersbook.com to make sure it works
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

# if the entered number is less than or equal to 1
# then it is not prime number
else:
    print(number, "is not a prime number")

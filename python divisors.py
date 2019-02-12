Katylub, exercise 3
# Write a program that prints all numbers between 1,000 and 10,000 that are divisible
# by 6 but not 12.

nl=[]
for x in range(1000, 10000):
    if (x%6==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))
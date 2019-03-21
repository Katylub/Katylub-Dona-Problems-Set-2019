# Katylub, exercise 3
# Write a program that prints all numbers between 1,000 and 10,000 that are divisible
# by 6 but not 12.

# I did research in the Python Tutorial and took as reference Stackoverflow (https://stackoverflow.com/questions/36760764/basic-python-for-loop)

nl=[]
for x in range(1000, 10000):
    if (x%6==0) and (x%12!=0):
        nl.append(str(x))
print (','.join(nl))

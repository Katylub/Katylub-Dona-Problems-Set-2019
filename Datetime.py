#Katylub, Exercise 8
#Write a program that outputs today’s date and time in the format ”Monday, January
# 10th 2019 at 1:15pm”.

#I did research, including training video, python tutorial web and I also used www.w3schools.com

#Import the date
import datetime
# give a name for the current date
x = datetime.datetime.now()
#print using the appropiate code
print(x.strftime("%A, %B %dth %Y at %H:%M%p"))
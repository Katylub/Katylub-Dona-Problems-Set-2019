#Katylub, Exercise 8
#Write a program that outputs today’s date and time in the format ”Monday, January
# 10th 2019 at 1:15pm”.

import datetime

x = datetime.datetime.now()

print(x.strftime("%A, %B %dth %Y at %H:%M%p"))
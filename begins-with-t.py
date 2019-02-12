# Katylub, exercise 2
# Write a program that outputs whether or not today is a day that begins with the
# letter T.

l = datetime.date.today().strftime("%A")

if l == ('Tuesday', 'Thursday'):
	print("Yes - today begins with a T.")
elif l == ('Monday', 'Wednesday', 'Friday', 'Saturday', 'Sunday'):
	print("No - today does not begin with a T.") 
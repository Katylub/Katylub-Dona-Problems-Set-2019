# Katylub, exercise 2
# Write a program that outputs whether or not today is a day that begins with the
# letter T.

l = datetime.date.today().strftime("%A")

if l in ('Tuesday', 'Thursday'):
	print("Yes - today begins with a T.")
else l == ('Monday', 'Wednesday', 'Friday', 'Saturday', 'Sunday'):
	print("No - today does not begin with a T.") 
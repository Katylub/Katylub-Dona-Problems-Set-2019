# Katylub Dona, exercise 10
#Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4].

import numpy as np
import matplotlib.pyplot as plt

# Research about Matlab in more than 10 web sites

x = np.arange (0,4)
#first function
y = x
#Second function
g = x*x
#Third function
h = 2**x

plt.plot(x, y, x, g, x, h)

plt.show()
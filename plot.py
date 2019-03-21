# Katylub Dona, exercise 10
#Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4].



x = [0:1:100];
y = x;
g = x*x
h = 2.^x;
plot(x, y, x, g, x, h, '.-'), legend('f(x)', 'f(x*x)', 'f(2.^x)')
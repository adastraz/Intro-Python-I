"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

# Use the 'format' string method to print the same thing
print('x is', str(x) + ', y is', str(y) + ', and z is', z)
# Finally, print the same thing using an f-string
print('x is {0:2d}, y is {1:3.2f}, and z is {2:s}'.format(x, y, z))
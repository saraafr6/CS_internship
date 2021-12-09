'''MANIPULATING STRINGS AND NUMBERS In the Python shell, create some string and number variables (integers, floats, and complex numbers).
Experiment a bit with what happens when you do operations with them,
including across types. Can you multiply a string by an integer, for example,
or can you multiply it by a float or complex number? Also load the math module and try a few of the functions; then load the cmath module and do the
same. What happens if you try to use one of those functions on an integer or
float after loading the cmath module? How might you get the math module
functions back?'''

import math,cmath
x=6
y="hello"
print(x*y)#hellohellohellohellohellohello
#print(3.5*y)#TypeError: can't multiply sequence by non-int of type 'float'
#print((3+2j)*y)#TypeError: can't multiply sequence by non-int of type 'complex'
print("math.ceil(3.4):",math.ceil(3.4))
print("math.cos(30):",math.cos(30))
print("math.factorial(8):",math.factorial(8))#factorial() only accepts integral values
print("math.pow(5, 2.4):",math.pow(5, 2.4))
print("cmath.sin(2+3j):",cmath.sin(2+3j))


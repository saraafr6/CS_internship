'''QUICK CHECK: MODULES Suppose that you have a module called new_math
that contains a function called new_divide. What are the ways that you
might import and then use that function? What are the pros and cons of each
method?
'''
#1
'''import new_math
x = new_math.new_divide(2)

The module name must be used to access the functions
'''

# 2
'''
from new_math import new_divide
y = new_divide(2)

One or more functions can be used without using the module name
'''


# 3
'''
from new_math import *
z = new_divide(2)

All names and functions can be accessed without using the module name BUT Not highly recommended
'''


'''Suppose that the new_math module contains a function call
_helper_math(). How will the underscore character affect the way that
_helper_math() is imported?'''

#when we use import * It won’t be imported


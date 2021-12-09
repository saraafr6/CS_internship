'''TRY THIS: VARIABLES AND EXPRESSIONS In the Python shell, create some variables.
What happens when you try to put spaces, dashes, or other nonalphanumeric characters in the variable name?
'''

#-x=12 SyntaxError: invalid syntax
#5x=12 SyntaxError: invalid syntax
#x !=12 SyntaxError: invalid syntax

_x=12 #True
x234=12 #True
x_y=12#True
'''نام متغیر باید یا با یک حرف انگلیسی، یا کاراکتر «_» شروع شود
در نام متغير فقط استفاده از حروف انگليسي اعداد و کاراکتر _ مجاز ميباشد
'''


'''Play around with a few complex expressions, such as x = 2 + 4 * 5 – 6 / 3.
Use parentheses to group the numbers in different ways and see how the result changes compared with the original ungrouped expression
'''
x = (2 + 4) * ((5 - 6) / 3)
y = 2 + 4 * (5 - 6) / 3
print(x,y)

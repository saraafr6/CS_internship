'''QUICK CHECK: FUNCTIONS AND PARAMETERS How would you write a function
that could take any number of unnamed arguments and print their values out
in reverse order?

?'''
def reverse(*value):
    for i in reversed(value):
        print(i)
reverse(8,9,10,11)

'''What do you need to do to create a procedure or void function—that is, a
function with no return value?'''

def x():
    x=2
x()

    
'''What happens if you capture the return value of a function with a variable?'''
#خروجي همان متغيرر خواهد بود و ميتوانيم از آن استفاده کنيم 

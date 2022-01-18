'''How would you modify the code for the decorator function to remove unneeded messages and enclose the return value of the
wrapped function in "<html>" and "</html>", so that myfunction
("hello") would return "<html>hello<html>"?'''

def decorate(func):
    def wrapper_func(*args):
        print(f"<html>{func(*args)}</html>")
    return wrapper_func

@decorate
def myfunction(parameter):
    return parameter

myfunction("hello")

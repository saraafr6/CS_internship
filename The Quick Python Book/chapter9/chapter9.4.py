'''Assuming that x = 5, what will be the value of x after funct_1() below executes? After funct_2() executes?
def funct_1():
x = 3
def funct_2():
global x
x = 2'''

x=5
def funct_1():
    x = 3
def funct_2():
    global x
    x = 2

funct_1()
print("after funct_1:",x)
funct_2()
print("after funct_2:",x)

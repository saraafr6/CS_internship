'''What would you need to modify in the previous code for the function four()to make it work for any number? '''

def four(number):
    x = 0
    while x < number:
      print("in generator, x =", x)
      yield x
      x += 1
for i in four(10):
    print(i)

'''What would you need to add to allow the starting point to also be set?'''
print("---------------------")
def four_start(x,y):
    while x<y:
      print("in generator, x =", x)
      yield x
      x+=1
for i in four_start(6,12):
    print(i)

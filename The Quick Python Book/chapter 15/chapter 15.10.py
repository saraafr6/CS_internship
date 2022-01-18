#Update the dimensions of the Rectangle class to be properties with getters and setters that don’t allow negative sizes.
class Rectangle:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
    @property    
    def x(self):
        return self.__x
    
    @property    
    def y(self):
        return self.__y

    @x.setter
    def x(self,x_new):
        if x_new>0:
          self.__x=x_new
        else:
            print("You can not use negative numbers")
          
    @y.setter
    def y(self,y_new):
        if y_new>0:
          self.__y=y_new
        else:
            print("You can not use negative numbers")  

r1=Rectangle(2,4)
print(r1.x)
print(r1.y)
r1.x=7
r1.y=-6
print("new x:",r1.x)
print("new y :",r1.y)

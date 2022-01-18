'''TRY THIS: INSTANCE VARIABLES AND METHODS Update the code for a Rectangle class so that you can set the dimensions when an instance is created, just
as for the Circle class above. Also, add an area() method'''
class Rectangle():
    def __init__(self,x=1,y=2):
        self.x=x
        self.y=y
    def area(self):
        return self.x * self.y

r1=Rectangle(3,5)

print(r1.area())

r2=Rectangle()
r2.x=6
r2.y=4

print(r2.area())



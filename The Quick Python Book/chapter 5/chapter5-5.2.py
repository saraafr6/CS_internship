#LIST SLICES AND INDEXES Using what you know about the len()function and list slices, how would you combine the two to get the second half of a list when you don’t know what size it is? 
import random
x=[1,3,2,4,8,7]
y=random.sample(range(0,100),random.randint(1,60))
n = int(input("Enter number of elements : "))
z=[]
for i in range(0, n):
     item= int(input())
 
     z.append(item)

print('list: ', z)
print("result:",z[(len(z)//2):])

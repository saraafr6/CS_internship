#What list comprehension would you use to process the list x so that all negative values are removed?
x=[0,2,-5,9,-1,4,-8]
y=[n for n in x if n>=0]
print(y)


'''Create a generator that returns only odd numbers from 1 to 100. (Hint: A
number is odd if there is a remainder if divided by 2; use % 2 to get the
remainder of division by 2.)'''
generator=(number for number in range(0,100) if number%2==1)
for number in generator:
    print(number,end="-")



#Write the code to create a dictionary of the numbers and their cubes from 11 through 15.   
x={item:item**3 for item in range(11,16)}
print("\n",x)

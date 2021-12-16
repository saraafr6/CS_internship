##Suppose that you have a list x = [1,3, 5, 0, -1, 3, -2], and you need to remove all negative numbers from
##that list. Write the code to do this.
mylist=[1,3,5,0,-1,3,-2]
new=list(filter(lambda x:x>=0 , mylist))
print(new)

for num in mylist:
    if num<0:
        mylist.remove(num)
print("new list:",mylist)        




##How would you count the total number of negative numbers in a list
##y = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]?
y=[[1, -1, 0], [2, 5, -9], [-2, -3, 0]]
count=0
for list in y:
    for item in list:
        if item<0:
            count+=1
print("count:",count)


##What code would you use to print very low if the value of x is below -5, low
##if it’s from -5 up to 0, neutral if it’s equal to 0, high if it’s greater than 0 up
##to 5, and very high if it’s greater than 5?
x=int(input("enter value of x\n"))
if x < -5:
    print("very low")
elif x < 0:
    print("low")
elif x==0:
    print("neutral")
elif x <= 5:
    print("high")
else:
    print("very high")

#MODIFYING LISTS Suppose that you have a list 10 items long. How might you move the last three items from the end of the list to the beginning, keeping them in the same order?
list1=[1,2,3,4,5,6,7,8,9,10]
list2=list1[-3:]
del list1[-3:]
list2.extend(list1)
print(list2)

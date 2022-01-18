'''QUICK CHECK: MUTABLE FUNCTION PARAMETERS What would be the result of changing a list or dictionary that was passed into a function as a parameter
value? Which operations would be likely to create changes that would be visible outside the function?
What steps might you take to minimize that risk?'''
#عملياتي مثل حذف و اضافه کردن و آپديت باعث تغيير در آنها ميشود
my_list1=[1,2,3,4]
my_list2=[1,2,3,4]
my_dict1={1:1,2:4,3:9}
my_dict2={1:1,2:4,3:9}
def add(x):
    x.append(5)
    print(x)
add(my_list1)
print(my_list1)


add(my_list2.copy())


def remove(y):
    y.pop(y[1])
    print(y)
    
remove(my_dict1)
print(my_dict1)

remove(my_dict2.copy())
print(my_dict2)

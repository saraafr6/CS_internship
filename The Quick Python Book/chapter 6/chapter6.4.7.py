"""Suppose that you have a list of strings in whichsome (but not necessarily all) of the strings begin and end with the double
quote character:
x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']
What code would you use on each element to remove just the double quotes?
"""
x = ['"abc"', "def", '"ghi"', '"klm"', "nop"]
y = []

for element in x:
    if element.startswith('"') and element.endswith('"'):
        y.append(element.strip('"'))
    else:
        y.append(element)
x = y
print(x)

"""for element in x:
    y.append(element.strip('"'))
print(y)"""

##What code could you use to find the position of the last p in Mississippi?
##When you’ve found that position, what code would you use to remove just
##that letter?

'''a = "Mississippi"
print(a.rfind("p"))
b = a.replace("pp", "p")
print(b)'''

a = "Mississippi"
b= a.rfind("p")
print(a[:b]+a[b+1:])

"""What would be the result of len([[1,2]] * 3)? What are two differences between using the in operator and a list’s index()
method?
Which of the following will raise an exception?: min(["a", "b”, "c"]); max([1, 2, "three"]); [1, 2, 3].count("one")
"""

print("len([[1,2]] * 3):",len([[1,2]] * 3)) #result=3

#in operator return true or false
#index() return index of element
x=[1,2,3]
print(1 in x , x.index(1))
#print(6 in x , x.index(6)) if element was not in list (in) operator return false but index() raise a ValueError: 6 is not in list
print("min['a', 'b', 'c'] is:",min(["a", "b", "c"]))
# max([1, 2, "three"])error
print("[1, 2, 3].count('one'):",[1, 2, 3].count("one"))

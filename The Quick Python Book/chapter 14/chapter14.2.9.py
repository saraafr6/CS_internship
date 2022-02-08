'''QUICK CHECK: EXCEPTIONS Do Python exceptions force a program to halt?
no we can handle exception and don't let it halt

Suppose that you want accessing a dictionary x to always return None if a key
doesn’t exist in the dictionary (that is, if a KeyError exception is raised).
What code would you use?'''

x={"a":1,"b":2, "c":3}
try:
    y=x["d"] #y=x[key]
except KeyError:
    y=None
print(y)


#TRY THIS: EXCEPTIONS What code would you use to create a custom ValueTooLarge exception and raise that exception if the variable x is over 1000?
class ValueTooLarge(Exception):
    pass
x=int(input("Enter a number"))
if x > 1000:
    raise ValueTooLarge("x can not be more than 1000")

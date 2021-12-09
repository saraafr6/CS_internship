'''GETTING INPUT Experiment with the input() function to get string and integer input.
Using code similar to the previous code, what is the effect of not using int() around the call to input()for integer input?
Can you modify that code to accept a float—say, 28.5?
What happens if you deliberately enter the wrong type of value?
Examples include a float in which an integer is expected and a string in which a number is expected—and vice versa.
'''
a=input("Enter string:")
print(a)

b=input("Enter integer:")#string
print(int(b)==b)


c=input("Enter float:")#string
print(float(c)==c)


d=int(input("Enter integer:"))#if Enter float--->ValueError: invalid literal for int() with base 10: '67.9'
print(int(d)==d)


e=float(input("Enter float:"))#if Enter integr--->True
print(float(e)==e)

'''TRY THIS: CATCHING EXCEPTIONS Write code that gets two numbers from the
user and divides the first number by the second. Check for and catch the
exception that occurs if the second number is zero (ZeroDivisionError).'''

num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
try:
    div=num1/num2
    print(div)
    
except ZeroDivisionError:
    print("Can't divide by zero.")
    

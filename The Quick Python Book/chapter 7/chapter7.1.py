'''Write the code to ask the user for three names and three ages. After the names and ages are entered, ask the user for
one of the names, and print the correct age.'''
x={input("enter first name\n"):int(input("enter first age\n")) ,input("enter second name\n"):int(input("enter second age\n")) , input("enter Third name\n"):int(input("enter Third age\n"))}
y=input("enter one of the names\n")
for key in x:
    if y==key:
        print(x[key])
        
               

    

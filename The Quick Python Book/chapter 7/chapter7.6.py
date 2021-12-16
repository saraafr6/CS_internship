'''Suppose that you’re writing a program that works like a spreadsheet. How might you use a dictionary to store the contents of a sheet? Write some sample code to both store a value and retrieve a
value in a particular cell. What might be some drawbacks to this approach?'''

x=dict()
x[(1,"a")]="names"
x[(1,"b")]="ages"
x[(3,"a")]="ali"
x[(3,"b")]=26
x[(2,"a")]="amir"
x[(2,"b")]=25
x[(4,"a")]="reza"
x[(4,"b")]=24
print(x)
print(x[(3,"a")])
print(x[(2,"b")])


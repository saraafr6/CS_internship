# Which of the following will not be converted to numbers

#print(int("a1")) #invalid literal for int() with base 10: 'a1'
print(int("12G", 16)) #Can’t interpret
print(float("12345678901234567890"))
print(int("12*2"))
# print(eval("12*2"))

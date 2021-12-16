"""TUPLES Explain why the following operations aren’t legal for
the tuple x = (1, 2, 3, 4):
x.append(1)
x[1] = "hello"
del x[2]
If you had a tuple x = (3, 1, 4, 2), how might you end up with x sorted?"""
# tuples are immutable
x = (3, 1, 4, 2)
print("sorted tuple is:", tuple(sorted(x)))

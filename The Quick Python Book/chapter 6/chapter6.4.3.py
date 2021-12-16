##If the string x equals "(name, date),\n", which of
##the following would return a string containing "name, date"?

x = "(name, date),\n"

print(x.rstrip("),"))
##'(name, date),\n'

print(x.strip("),\n"))
##'(name, date'

print(x.strip("\n(,)"))

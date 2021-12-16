# What would be a quick way to change all punctuation in a string to spaces?
import string

str1 = "hello, world!(?)."
punctuation = string.punctuation
str2 = str1.maketrans(punctuation, " " * len(punctuation))
str3 = str1.translate(str2)
print(str3)

"""
WORD COUNTING
In the previous lab, you took the text of the first chapter
of Moby Dick, normalized the case, removed punctuation, and wrote the
separated words to a file. In this lab, you read that file, use a dictionary to
count the number of times each word occurs, and then report the most common
and least common words.
"""
x=dict()
y=[]
with open("moby_01_clean.txt", "r") as infile:
    for line in infile:
            y.append(line.strip())
    for word in y:
        x[word]=x.get(word, 0) + 1
        
'''for i in y:
    x[i]=y.count(i)'''
newlist = list(x.items())
newlist.sort(key= lambda x:x[1])
print(newlist[0],newlist[-1])

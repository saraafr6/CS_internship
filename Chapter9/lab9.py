'''Looking back at the labs in chapters 6 and 7, refactor that code into functions for cleaning and processing the data. The goal
should be that most of the logic is moved into functions. Use your own judgment as to the types of functions and parameters, but keep in mind that functions should do just one thing, and they shouldn’t have any side effects that
carry over outside the function.'''

def lower(line):
    lowline = line.lower()
    return lowline

def del_punct(line):
    rempunct=line.maketrans(".,?!:;","      ")
    remove_punctuation=line.translate(rempunct)
    return remove_punctuation

def words(line):    
    words = line.split()
    cleaned_words= "\n".join(words)
    return cleaned_words

with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
    for line in infile:
      lower_line=lower(line)
      cleaned_line=del_punct(lower_line)    
      word=words(cleaned_line)
      outfile.write(word)
      
def count(y):
    x={}
    for word in y:
        x[word]=x.get(word, 0) + 1
    return x  
  
def most_least(x):
    newlist = list(x.items())
    newlist.sort(key= lambda x:x[1])
    print(newlist[0],newlist[-1])


y=[]      
with open('moby_01_clean.txt') as infile:
    for word in infile:
            y.append(word.strip())
            
words_count=count(y)
common_words=most_least(words_count)

    

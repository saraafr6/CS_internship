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

def count(y):
    x={}
    for word in y:
        x[word]=x.get(word, 0) + 1
    return x  
  
def most_least(x):
    newlist = list(x.items())
    newlist.sort(key= lambda x:x[1])
    print(newlist[0],newlist[-1])

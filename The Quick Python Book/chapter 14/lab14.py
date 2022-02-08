'''CUSTOM EXCEPTIONS
Think about the module you wrote in chapter 9 to count word frequencies. What errors might reasonably occur in those functions?
Refactor those functions to handle those exception conditions appropriately.'''



def lower(line):
    try:
      lowline = line.lower()
    except AttributeError:
      print("empty line")
         
    return lowline

def del_punct(line):
    try:
      rempunct=line.maketrans(".,?!:;","      ")
      remove_punctuation=line.translate(rempunct)
    except AttributeError:
      print("empty line")  
    return remove_punctuation

def words(line):
    try:
       words = line.split()
       cleaned_words= "\n".join(words)
    except AttributeError:
        print("line and word not found")
    return cleaned_words
try:
    with open("1.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
        for line in infile:    
          lower_line=lower(line)
          cleaned_line=del_punct(lower_line)    
          word=words(cleaned_line)
          outfile.write(word)
except FileNotFoundError:
    print("The file you are looking for could not be found. ")
    
      
def count(y):
    x={}
    for word in y:
        x[word]=x.get(word, 0) + 1
    return x  
  
def most_least(x):
    newlist = list(x.items())
    newlist.sort(key= lambda x:x[1])
    try:
       print(newlist[0],newlist[-1])
    except IndexError:
        print(" Index not found, make sure your file is not empty")

y=[]      
with open('moby_01_clean.txt') as infile:
    for word in infile:
            y.append(word.strip())
            
words_count=count(y)
common_words=most_least(words_count)

    

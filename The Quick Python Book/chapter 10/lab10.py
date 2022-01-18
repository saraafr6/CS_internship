'''Package the functions created at the end of chapter 9 as a standalone module. Although you can include code to run the module as the main program, the goal should be for the functions to be
completely usable from another script.'''
import functions

with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
    for line in infile:
      lower_line=functions.lower(line)
      cleaned_line=functions.del_punct(lower_line)    
      word=functions.words(cleaned_line)
      outfile.write(word)

y=[]      
with open('moby_01_clean.txt') as infile:
    for word in infile:
            y.append(word.strip())
            
words_count=functions.count(y)
common_words=functions.most_least(words_count)      

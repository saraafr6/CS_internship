
# LAB 8: REFACTOR WORD_COUNT Rewrite the word-count program from section 8.7 to make it shorter.
# You may want to look at the string and list operations already discussed, as well as think about different ways
# to organize the code.
# You may also want to make the program smarter so that only alphabetic strings
# (not symbols or punctuation) count as words.
line_count, word_count,char_count =0,0,0
with open('word_count.tst') as infile:
 for line in infile:
   newline=line.maketrans(",.)(/!?:;","         ")
   lines=line.translate(newline)
   print(lines)
   line_count+=1
   words=lines.split()
   word_count+=len(words)
   char_count += len(lines)
print("File has {0} lines, {1} words, {2} characters".format
(line_count, word_count, char_count))

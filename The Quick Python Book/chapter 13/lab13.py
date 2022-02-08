'''LAB 13: FINAL FIXES TO WC If you look at the man page for the wc utility, you
see two command-line options that do very similar things. -c makes the utility
count the bytes in the file, and -m makes it count characters (which in the
case of some Unicode characters can be two or more bytes long). In addition,
if a file is given, it should read from and process that file, but if no file is given,
it should read from and process stdin.
Rewrite your version of the wc utility to implement both the distinction
between bytes and characters and the ability to read from files and standard
input.'''
import sys,os
line_count, word_count,char_count =0,0,0
myfile=input("file name?")

if os.path.exists(myfile):
    mf=input("If you want to open the file in binary mode, please enter -c and otherwise enter -m : ")
    file=myfile
    if mf == "-c":
       mode = "rb"
    if mf == "-m":
       mode = "r"
    with open(file,mode) as infile:
      for line in infile:
        line_count+=1
        word_count+=len(line.split())
        char_count += len(line)
      if mf == "-c":
        print("file has {} byte".format(char_count))
      else:  
        print("file has {} char".format(char_count))
else:
    file = sys.stdin.readlines()
    for line in file:
        line_count+=1
        word_count+=len(line.split())
        char_count += len(line)
    print("file has {} char".format(char_count))    
      
print("file has {} word".format(word_count))
print("file has {} line".format(line_count))      
        


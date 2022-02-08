'''QUICK CHECK: What is the significance of adding a "b" to the file open mode
string, as in open("file", "wb")?

it means you open this file in binary mode

'''

#Suppose that you want to open a file named myfile.txt and write additional data on the end of it. What command would you use to open
#myfile.txt?

f=open("myfile.txt","a")
f.write("hello World!")
f.close()
#What command would you use to reopen the file to read from the beginning
f=open("myfile.txt","r")




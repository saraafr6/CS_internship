'''How might you calculate the total size of all files ending with .txt that aren’t symlinks in a directory? If your first answer
was using os.path, also try it with pathlib, and vice versa.
'''
import os
import pathlib
path=os.getcwd()
size1 = 0
for file in os.listdir(path):
    if not os.path.islink(path):
        if ".txt" in os.path.basename(file):
           size1 += os.path.getsize(file)
print(size1)




path2 = pathlib.Path.cwd()
size2=0
for file in path2.glob("*.txt"):
    if not file.is_symlink():
        with open(file) as f:
         size2 += f.seek(0,2)

print(size2)

#Write some code that builds off your solution to move the same .txt files in the lab question to a new subdirectory called backup in the same directory

import pathlib,os,shutil
path = pathlib.Path.cwd()
size3 = 0

for file in path.glob("*.txt"):
    if not file.is_symlink():
         new_path=path.joinpath("backup")
         path2=os.path.join(new_path,file)
         print(path2)
         size3 += os.path.getsize(file)
         shutil.move(file,new_path)
print(size3)


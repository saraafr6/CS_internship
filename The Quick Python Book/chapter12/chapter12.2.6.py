"""
MANIPULATING PATHS
How would you use the os module’s functions to take a path to a file called test.log and create a new file path
in the same directory for a file called test.log.old? 
"""
import os
cwd_path = os.getcwd()
print(cwd_path)
path1 = os.path.join(cwd_path, 'test.log')
print("os_new1:",path1)
path2 = os.path.join(cwd_path, 'test.log.old')
print("os_new2:",path2)


'''How would you do the same thing using the pathlib module?'''

from pathlib import Path
cwd_path=Path.cwd()
print(cwd_path)
path1 = Path.joinpath(cwd_path, 'test.log')
print("pathlib_new1:",path1)
path2 = Path.joinpath(cwd_path, 'test.log.old')
print("pathlib_new2:",path2)


'''What path would you get if you created a pathlib Path object from os.pardir? Try it and find out.'''

my_path= Path(os.pardir)
print("os.pardir:",my_path)
print(Path().joinpath(os.pardir, 'text.log'))
#print(my_path.absolute())


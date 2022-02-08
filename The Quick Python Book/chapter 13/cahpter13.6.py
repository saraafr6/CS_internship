'''TRY THIS: REDIRECTING INPUT AND OUTPUT Write some code to use the mio.py module in listing 13.1 to capture all the print output of a script to a file
named myfile.txt, reset the standard output to the screen, and print that file to screen.'''

import mio


mio.capture_output("myfile.txt")
print("hello")
print(1 + 3)
mio.restore_output()
print(2)
mio.print_file("myfile.txt")

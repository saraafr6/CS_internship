import sys
_file_object = None
def capture_output(file="capture_file.txt"):
       """capture_output(file='capture_file.txt'): redirect the standard output to 'file'."""
       global _file_object
       global old_std
       print("output will be sent to file: {0}".format(file))
       print("restore to normal by calling 'mio.restore_output()'")
       _file_object = open(file, 'w')
       old_std=sys.stdout
       sys.stdout = _file_object
def restore_output():
      """restore_output(): restore the standard output back to thedefault (also closes the capture file)"""
      global _file_object
      sys.stdout = old_std
      _file_object.close()
      print("standard output has been restored back to normal")
def print_file(file="capture_file.txt"):
      """print_file(file="capture_file.txt"): print the given file to thestandard output"""
      f = open(file, 'r')
      print(f.read())
      f.close()
def clear_file(file="capture_file.txt"):
      """clear_file(file="capture_file.txt"): clears the contents of thegiven file"""
      f = open(file, 'w')
      f.close()

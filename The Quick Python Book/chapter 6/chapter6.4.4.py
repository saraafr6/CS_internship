#If you wanted to check whether a line ends with the string "rejected", what string method would you use? Would there be any other ways to get the same result?

import re

x="Your file has been rejected"
print(x.endswith("rejected"))


y=x[-(len("rejected")):]
if y=="rejected":
    print("True")
else:
    print("False")

    
z= re.search("rejected$", x)

if z:
  print("True")
else:
  print("False")

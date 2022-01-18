'''HTML CLASSES In this lab, you create classes to represent an HTML
document. To keep things simple, assume that each element can contain only
text and one subelement. So the <html> element contains only a <body> element, and the <body> element contains (optional) text and a <p> element
that contains only text.
The key feature to implement is the __str__() method, which in turn calls
its subelement's __str__() method, so that the entire document is returned
when the str() function is called on an <html> element. You can assume
that any text comes before the subelement

Here’s example output from using the classes:
para = p(text="this is some body text")
doc_body = body(text="This is the body", subelement=para)
doc = html(subelement=doc_body)
print(doc)
<html>
<body>
This is the body
<p>
this is some body text
</p>
</body>
</html>
'''


class html:
    def __init__(self, text=None, subelement=None):
        self.text=text
        self.subelement=subelement
        
    def __str__(self):
        string='<%s> \n' %(self.__class__.__name__)
        if self.text != None:
            string+= str(self.text)
        if self.subelement !=None:
            string += str(self.subelement)
        string+='\n</%s>' %(self.__class__.__name__)    
        return string
    
class body:
    def __init__(self,text=None, subelement=None):
        self.text=text
        self.subelement=subelement
        
    def __str__(self):
        string='<%s> \n' %(self.__class__.__name__)
        if self.text != None:
            string+= str(self.text)
        if self.subelement !=None:
            string += str(self.subelement)
        string+='\n</%s>' %(self.__class__.__name__)    
        return string
class p:
    def __init__(self,text):
        self.text=text 
    def __str__(self):
        string='\n<%s> \n' %(self.__class__.__name__)
        if self.text != None:
            string+= str(self.text)
        string+='\n</%s>' %(self.__class__.__name__)    
        return string    

para = p(text="this is some body text")
doc_body = body(text="This is the body", subelement=para)
doc = html(subelement=doc_body)
print(doc)

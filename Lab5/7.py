import re

def textxasx(text):
    h=''
    d=re.sub('_',' ',text)
    d=d.title()
    d=re.sub(' ','',d)
    return d

text=input()
print(textxasx(text))
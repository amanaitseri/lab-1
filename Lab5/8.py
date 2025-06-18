import re

def textxx(text):
    h=''
    text=re.split("[A-Z]",text)

    return text


print(textxx('abcAabc'))
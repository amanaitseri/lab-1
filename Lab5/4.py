import re

text = input()
tx = re.findall('^[A-Z]+[a-z]+$',text)

print(*tx)
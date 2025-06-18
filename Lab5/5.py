import re

text = input() # cdab
tx = re.search('^a.+b\Z',text)

print(tx)
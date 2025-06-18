import re

text = input()
tx = re.findall('[a-z]+_[a-z]+$',text)

print(tx)       
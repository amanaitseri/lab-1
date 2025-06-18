import re

text = input()
tx = re.sub('[ ,.]', ':', text)
print(tx)
import re
text = input()
tx = re.findall('^a(b{2,3})')
print(tx)
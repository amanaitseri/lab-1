import os

path=r'C:\Users\Lenovo\Desktop\wor.txt'

if os.path.exists(path):
    print(os.path.basename(path))
    print(os.path.dirname(path))
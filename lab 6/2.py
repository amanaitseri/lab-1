import os

path=r'C:\Users\Lenovo\Desktop\wor.txt'

print(os.access(path,os.F_OK))

print(os.access(path,os.R_OK))

print(os.access(path,os.W_OK))

print(os.access(path,os.X_OK))


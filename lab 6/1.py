import os
b=r'C:\Users\Lenovo\Desktop'
a=[]
for x in os.listdir(b):
    if os.path.isfile(os.path.join(b, x)):
        a.append(x)

for i in a:
    print(a)
def gene(n,k):
    for i in range(n,k):  
        yield i**2


for i in gene(int(input()),int(input())):
    print(i)

def gene(dad):
    for i in range(dad):
        yield i**2


for i in gene(int(input())):
    print(i)
f=open('1.txt')
x=f.readlines()

for k in x:
    k=k.strip('[]\n ')
    k=k.split()
    print k[0], k[1]

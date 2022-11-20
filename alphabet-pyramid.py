n = 10
asci = 65
for i in range(n):
    for j in range(i,n):
        print(" ",end='')
    for k in range(i+1):
        alphabet = chr(asci)
        print(alphabet,end=' ')
        asci+=1
    print()
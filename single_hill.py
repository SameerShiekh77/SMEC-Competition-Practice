n = 5
for i in range(n):
    for j in range(i,n):
        print(" ",end='')
    for k in range(i):
        print("*",end='')
    for l in range(i+1):
        print("*",end='')
    print()
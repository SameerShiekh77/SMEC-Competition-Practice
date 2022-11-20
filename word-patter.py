string = input("Enter a word: ")
for i in range(len(string)):
    for j in range(i+1):
        print(string[j],end='')
    print()
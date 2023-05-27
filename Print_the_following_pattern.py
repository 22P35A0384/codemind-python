n = int(input())
for i in range(n):
    for j in range(n):
        if j==i or j==n-1-i:
            print(n-i,"",end="")
        else:
            print(" ",end="")
    print()
n = int(input())
for i in range(n):
    for j in range(n):
        if j==i or j == n-i-1:
            print("x",end="")
        else:
            print(0,end="")
    print()
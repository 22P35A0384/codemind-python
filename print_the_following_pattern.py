n = int(input())
l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(n):
    for j in range(n-i):
        print(l[n-i-1],end=" ")
    print()
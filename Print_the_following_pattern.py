n = int(input())
l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(1,n+1):
    for k in range(n-i):
        print(' ',end='')
    for j in range(i):
        print(l[j],end="")
    for a in range(i-1):
        print(l[i-2-a],end="")
    print()
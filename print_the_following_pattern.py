n = int(input())
for i in range(n):
    for l in range(n-i-1):
        print(" ",end="")
    for k in range(i,0,-1):
        print(k,end="")
    for j in range(0,i+1):
        print(j,end="")
    print()
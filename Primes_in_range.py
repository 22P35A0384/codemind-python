def primenum(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            break
    else:
        return n
a = int(input())
b = int(input())
x = 0
for j in range(a,b+1):
    if j == 1:
        x-=1
    if primenum(j):
        x+=1
print(x)
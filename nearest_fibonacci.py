def fibonacci(n):
    a = 0
    b = 1
    l=[]
    for i in range(n):
        c = a+b
        l.append(c)
        a = b
        b = c
    if n in l:
        return n
n = int(input())
x = n
m = n
l = 0
s = 0
while True:
    if fibonacci(x):
        l = x
        break
    else:
        x+=1
while True:
    if fibonacci(m):
        s = m
        break
    else:
        m-=1
d1 = abs(l-n)
d2 = abs(n-s)
if d1==d2:
    print(s,l)
if d1<d2:
    print(l)
if d2<d1:
    print(s)
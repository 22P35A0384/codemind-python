def fibnacci(n):
    a = 0
    b = 1
    l = []
    e = 0
    while True:
        c = a+b
        l.append(c)
        a = b
        b = c
        e+=1
        if e==n-2:
            break
    print(0,1,*l)    
n = int(input())
fibnacci(n)
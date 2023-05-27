n = int(input())
if n>0:
    s = 0
    while n:
        r = n%10
        n = n//10
        s = s*10+r
    print(s)
else:
    s = 0
    m = -1*n
    while m:
        r = m%10
        m = m//10
        s = s*10+r
    x = -1*s
    print(x)
def gcd(a,b):
    r = min(a,b)
    while r:
        if a%r==0 and b%r==0:
            break
        r-=1
    return r
a,b = map(int,input().split())
x = gcd(a,b)
m = a*b
lcm = m/x
print("{:.0f}".format(lcm))
def sumdig(m):
    e = 0
    while m:
        x = m%10
        m = m//10
        e+=x
    return e
n = int(input())
m = n**2
if sumdig(m)==n:
    print("Neon Number")
else:
    print("Not Neon Number")
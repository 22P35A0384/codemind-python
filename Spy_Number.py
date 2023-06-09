def sumdig(n):
    e = 0
    while n:
        x = n%10
        n = n//10
        e+=x
    return e
def prddig(n):
    e = 1
    while n:
        x = n%10
        n = n//10
        e = e*x
    return e
n = int(input())
p = prddig(n)
s = sumdig(n)
if p==s:
    print("Spy Number")
else:
    print("Not Spy Number")
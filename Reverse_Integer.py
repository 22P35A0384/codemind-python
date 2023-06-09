def reverse(n):
    e = 0
    while n:
        x = n%10
        n = n//10
        e = e*10+x
    return e
n = int(input())
if n>0:
    print(reverse(n))
else:
    m = -1*n
    x = reverse(m)*-1
    print(x)
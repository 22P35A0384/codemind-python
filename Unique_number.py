def dig(n):
    l = []
    while n:
        x = n%10
        n = n//10
        l.append(x)
    for i in l:
        if l.count(i)==2:
            return "Not Unique Number"
            break
    else:
        return "Unique Number"
n = int(input())
print(dig(n))
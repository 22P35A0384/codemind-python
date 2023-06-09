def fibnocci(n):
    a = 0
    b = 1
    l = [0,1]
    for i in range(n):
        c = a+b
        a = b
        b = c
        l.append(c)
    if n in l:
        return "True"
    else:
        return "False"
n = int(input())
print(fibnocci(n))
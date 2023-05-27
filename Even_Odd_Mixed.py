n = int(input())
e=0
o=0
while n:
    r = n%10
    n = n//10
    if r%2==0:
        e+=1
    else:
        o+=1
if e==0:
    print("Odd")
elif o==0:
    print("Even")
else:
    print("Mixed")
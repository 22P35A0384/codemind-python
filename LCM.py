a,b = map(int,input().split())
x = max(a,b)
while True:
    if x%a==0 and x%b==0:
        lcm = x
        break
    x+=1
print(lcm)
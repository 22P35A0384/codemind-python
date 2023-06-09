n = int(input())
l = []
for i in range(n//2+1):
    if i*(i+1)==n:
        l.append(i)
if len(l)==0:
    print("NO")
else:
    print("YES")
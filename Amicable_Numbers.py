n = int(input())
m = int(input())
s1 = 0
s2 = 0
for i in range(1,n):
    if n%i==0:
        s1+=i
for j in range(1,m):
    if m%j==0:
        s2+=j
if n == s2 and m == s1:
    print("Amicable")
else:
    print("Not Amicable")
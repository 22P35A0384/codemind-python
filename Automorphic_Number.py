n = int(input())
print("Automorphic Number" if int(str(n**2)[-len(str(n))::]) == n else "Not an Automorphic Number")
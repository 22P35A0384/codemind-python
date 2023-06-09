def maximum69Number (num):
    maxi = -1
    numS = [i for i in str(num)]
    for i in range(len(numS)):
        if int(numS[i]) != 9:
            numS[i] = '9'
            maxi = max(maxi, int(''.join(numS)))
            numS[i] = '6'
    return maxi if maxi + 1 else num
n = int(input())
print(maximum69Number(n))
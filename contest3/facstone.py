import math
while True:
    x = int(input())
    if x == 0:
        break
    dec = int(x//10)
    power = dec - 196
    res = 2**(2+power)
    biggestuint = (2**res)-1
    n = 1
    l = 0
    r = int(math.sqrt(biggestuint))
    flag = True
    while l<r:
        n = (l+r)//2
        nfac = math.factorial(n)
        if nfac == biggestuint:
            flag = False
            print(n)
            break
        elif nfac > biggestuint:
            r = n-1
        else:
            l = n+1
    if flag:
        print(l)

    
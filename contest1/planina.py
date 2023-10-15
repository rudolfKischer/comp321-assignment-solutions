n = 5
curr = 2
for _ in range(n):
    curr = curr*2-1
print(curr**2)
'''n = int(input())


def planina(n):
    w = width(n)
    return w * w

def width(n):
    if n == 1:
        return 2
    
    return 2 * width(n-1) - 1

print(planina(n))'''
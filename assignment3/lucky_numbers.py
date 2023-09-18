n = int(input())

def build_luck_num(n,num):
    k = len(str(num))
    if num % k != 0:
        return 0
    if k == n:
        # print(num)
        return 1
    count = 0
    start = 0
    if num == 0:
        start = 1
    num = num * 10
    for i in range(start, 10):
        new_num = num + i
        count += build_luck_num(n, new_num)
    return count
            
print(build_luck_num(n,0))
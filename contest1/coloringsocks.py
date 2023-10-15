S,C,K = map(int, input().split())
sock_values = map(int, input().split())
table = {}
count = 0 # maybe should be 1?
for D in sock_values:
    diff = abs(K-D)
    if diff not in table:
        table[diff] = 1
        count +=1

    else:
        table[diff] += 1

    if table[diff] > C:
        count += 1
        table[diff] -= C # Or just reset to 1

print(count)

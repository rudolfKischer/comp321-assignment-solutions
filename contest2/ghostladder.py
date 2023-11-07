
inputl = [int(x) for x in input().split()]
n = inputl[0]
m = inputl[1]
dp = [[x for x in range(n)] for _ in range(m)]
for i in range(m):
    a = int(input())
    dp[i][a-1] = a
    dp[i][a] = a-1

sol = []
for i in range(n):
    curr = i
    for j in range(n-1):
        print(f'curr is {curr}')
        curr = dp[curr][j]
    print(f'final curr is {curr}')
    sol.append([i+1, curr+1])
    
sol = sorted(sol, key = lambda x : x[1])
print(sol)
for x in sol:
    print(x[0])
print(dp)
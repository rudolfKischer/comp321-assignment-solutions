weights=[1]
n=len(weights) 
if n==1:
    print(weights[0]) 
else:
    dp = [[0 for _ in range(2000)] for _ in range(n)]
    dp[0][weights[0]] = 1
    for i in range(1,n):
        dp[i][weights[i]]=1
        for j in range(2000):
            if dp[i-1][j]!=0:
                dp[i][j] = 1
                if j+weights[i]<2000:
                    dp[i][j+weights[i]]=1
    if dp[n-1][1000]==1:
        print(1000)
    else:
        for i in range(999):
            if dp[n-1][1000+i]==1:
                print(1000+i)
                break
            elif dp[n-1][1000-i]==1:
                print(1000-i)
                break
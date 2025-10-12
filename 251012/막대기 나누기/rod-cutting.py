n = int(input())
profit = list(map(int, input().split()))

# Please write your code here.
dp = [[0] * (n+1) for _ in range(n+1)] 

for i in range(1,n+1):
    for j in range(1, n+1):
        if j<i:
            continue
        
        val = 0 
        for k in range(1, i):
            val = max(val, dp[k][j-i])

        dp[i][j] = max(dp[i][j],val + profit[i-1], dp[i][j-i] + profit[i-1])

ans = 0

for i in range(n+1):
    ans = max(ans, max(dp[i]))

# for i in range(n+1):
#     print(dp[i])
print(ans)
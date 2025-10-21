n = int(input())
coin = [0] + list(map(int, input().split()))

# Please write your code here.
dp =[[0]*(4) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(4):
        if i == 1:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + coin[i])
            continue
        
        if j == 0 or j == 3:
            dp[i][j] = max(dp[i][j], dp[i-2][j] + coin[i])
            continue
        
        dp[i][j] =  max(dp[i][j], dp[i-2][j] + coin[i], dp[i-1][j-1] + coin[i])

# for d in dp:
#     print(d)

print(max(dp[n]))
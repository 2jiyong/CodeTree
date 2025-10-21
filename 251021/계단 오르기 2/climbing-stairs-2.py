n = int(input())
coin = [0] + list(map(int, input().split()))

# Please write your code here.
dp =[[0]*(4) for _ in range(n+1)]

dp[1][0] = 0
dp[1][1] = coin[1]
dp[1][2] = coin[1]
dp[1][3] = 0

for i in range(2, n+1):
    for j in range(4):
        if j == 0:
            dp[i][j] = max(dp[i][j], dp[i-2][j] + coin[i])
            continue
        
        dp[i][j] =  max(dp[i][j], dp[i-2][j] + coin[i], dp[i-1][j-1] + coin[i])

# for d in dp:
#     print(d)

print(max(dp[n]))
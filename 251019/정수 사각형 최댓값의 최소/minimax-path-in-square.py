n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dp = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0 :
            dp[i][j] = grid[i][j]
            continue
        if i == 0:
            dp[i][j] = max(dp[i][j-1], grid[i][j])
            continue
        if j == 0 :
            dp[i][j] = max(dp[i-1][j], grid[i][j])
            continue
        
        dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]), grid[i][j])


# for d in dp:
#     print(d)

print(min(dp[n-1]))

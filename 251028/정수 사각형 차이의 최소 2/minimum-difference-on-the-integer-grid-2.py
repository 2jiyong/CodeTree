n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# dp[i][j] = i,j 일때의 최대값

import sys
MAX = sys.maxsize
dp = [[0]*n for _ in range(n)]

def initialize_dp():
    dp[0][0] = grid[0][0]

    for r in range(1,n):
        dp[r][0] = max(dp[r-1][0], grid[r][0])
    
    for c in range(1,n):
        dp[0][c] = max(dp[0][c-1], grid[0][c])

def solve(lower_bound):
    for i in range(n):
        for j in range(n):
            if grid[i][j] < lower_bound:
                grid[i][j] = MAX
            
    initialize_dp()

    for i in range(1,n):
        for j in range(1,n):
            dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]), grid[i][j])


    return dp[n - 1][n - 1]

ans = MAX
for i in range(1,101):
    max_num = solve(i)

    if max_num == MAX:
        continue
    ans = min(ans,abs(max_num-i))

print(ans)

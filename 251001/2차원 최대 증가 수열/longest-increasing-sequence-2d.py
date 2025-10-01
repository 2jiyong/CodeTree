n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[0]*m for _ in range(n)]
dp[0][0] = 1
for r in range(n):
    for c in range(m):
        if r == 0 or c == 0 :
            continue
        
        for r1 in range(r):
            for c1 in range(c):
                if grid[r1][c1]<grid[r][c] and dp[r1][c1]!=0: 
                    dp[r][c] = max(dp[r][c], dp[r1][c1] + 1)
ans = 0
for r in range(n):
    ans = max(max(dp[r]),ans)
print(ans)



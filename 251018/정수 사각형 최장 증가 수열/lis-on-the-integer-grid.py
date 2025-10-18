n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# dpij를 해당 셀에서 갈 수 있는 최대값

dp = [[-1]*n for _ in range(n)]

dxs, dys = [1,-1,0,0], [0,0,1,-1]

def in_range(r,c):
    return r>=0 and r<n and c>=0 and c<n


def calc_count(r,c):
    if dp[r][c] != -1:
        return dp[r][c]
    
    num = 0 

    for dx,dy in zip(dxs,dys):
        nr = r+dx
        nc = c+dy
        if in_range(nr,nc) and grid[r][c] < grid[nr][nc]:
            num = max(num, calc_count(nr,nc))
    dp[r][c] = num + 1
    return num + 1
    

for i in range(n):
    for j in range(n):
        calc_count(i,j)

ans=0
for d in dp:
    ans = max(ans,max(d))
    
print(ans)

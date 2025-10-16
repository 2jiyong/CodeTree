n, m = map(int, input().split())
quests = [tuple(map(int, input().split())) for _ in range(n)]
quests.insert(0,0)
# Please write your code here.
import sys
MAX = sys.maxsize

dp = [[MAX]*(m+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(1,n+1):
    e = quests[i][0]
    t = quests[i][1]
    for j in range(m+1):
        dp[i][j] = min(dp[i][j], dp[i-1][j])

        if e<=j:
            dp[i][j] = min(dp[i][j], dp[i-1][j-e] + t)
        
        if j == m:
            if j-e < 0:
                e = j
            for k in range(j-e,j):
                dp[i][j] = min(dp[i][j], dp[i-1][k] + t)

# for d in dp:
#     print(d)
print(dp[n][m])


        

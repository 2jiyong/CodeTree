n, m = map(int, input().split())
quests = [tuple(map(int, input().split())) for _ in range(n)]
quests.insert(0,0)
# Please write your code here.
import sys
MAX = sys.maxsize

dp = [MAX]*(m+1)
dp[0] = 0

for i in range(1,n+1):
    e = quests[i][0]
    t = quests[i][1]
    for j in range(m,-1,-1):
        if j == m:
            val = j-e
            if val<0:
                val = 0 
            for k in range(val,j):        
                dp[j] = min(dp[j], dp[k] + t)
            continue         
        if e > j:
            continue
        dp[j] = min(dp[j], dp[j-e] + t)

if dp[m] == MAX:
    dp[m] = -1
print(dp[m])


        

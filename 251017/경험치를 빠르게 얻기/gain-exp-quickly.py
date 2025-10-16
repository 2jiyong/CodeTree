n, m = map(int, input().split())
quests = [tuple(map(int, input().split())) for _ in range(n)]
quests.insert(0,(0,0))
# Please write your code here.
import sys
MAX = sys.maxsize
a = 0
for q in quests:
    a+=q[0]

dp = [MAX]*(a+1)
dp[0] = 0

for i in range(1,n+1):
    e = quests[i][0]
    t = quests[i][1]
    for j in range(a,-1,-1):    
        if e > j :
            continue
        if dp[j-e] == MAX:
            continue
        dp[j] = min(dp[j], dp[j-e] + t)

# if dp[m] == MAX:
#     dp[m] = -1
print(min(dp[m:]))
# print(dp)

        

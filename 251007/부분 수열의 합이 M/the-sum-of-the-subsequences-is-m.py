n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

import sys

MAX = sys.maxsize
dp = [MAX]*(m+1)
dp[0] = 0 

for j in range(n-1,-1,-1):
    for i in range(m,-1,-1):
        if A[j] > i:
            continue
        if dp[i-A[j]] == MAX:
            continue
        dp[i] = min(dp[i-A[j]] + 1,dp[i])
if dp[-1] == MAX:
    dp[-1] = -1

print(dp[-1])

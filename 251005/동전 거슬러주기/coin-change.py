N, M = map(int, input().split())
coins = list(map(int, input().split()))

# Please write your code here.
import sys
MAXSIZE = sys.maxsize

dp = [MAXSIZE]*(M+1)
dp[0] = 0
for i in range(1, M+1):
    for coin in coins:
        if i < coin:
            continue
        dp[i] = min(dp[i-coin]+1, dp[i])
if dp[-1] == MAXSIZE:
    dp[-1] = -1

print(dp[-1])


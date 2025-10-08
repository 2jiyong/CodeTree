N, M = map(int, input().split())
coins = list(map(int, input().split()))

# Please write your code here.

dp = [0] * (M+1)

for i in range(1,M + 1):

    for coin in coins:
        if coin > i :
            continue
        if dp[i-coin] == 0 and i-coin != 0:
            continue
        dp[i] = max(dp[i], dp[i-coin] + 1)

if dp[M] == 0:
    dp[M] = -1

print(dp[M])


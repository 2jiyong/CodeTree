n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

segments.sort()

dp = [0]*n

# Please write your code here.

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if segments[i][0]>segments[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
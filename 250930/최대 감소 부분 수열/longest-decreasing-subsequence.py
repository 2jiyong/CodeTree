n = int(input())
m = list(map(int, input().split()))

# Please write your code here.
import sys
dp = [0]*n
# dp i 채우기
for i in range(n):
    val = 1
    # dp i 보다 작은애들 비교
    for j in range(i):
        if (m[j]>m[i]):
            val = max(val,dp[j]+1)
    dp[i] = val
print(max(dp))

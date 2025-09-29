n = int(input())
m = list(map(int, input().split()))

# Please write your code here.
dp = [0]*n

for i in range(n):
    val = 0
    for j in range(i):
        if (m[j]<m[i]):
            val = max(val,dp[j])
    dp[i] = val + 1
print(max(dp))   

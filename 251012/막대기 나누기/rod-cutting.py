n = int(input())
profit = list(map(int, input().split()))

# Please write your code here.
dp = [[0] * (n+1) for _ in range(n+1)] 

for i in range(1,n+1):
    for j in range(n+1):
        if j<i:
            continue
        
        dp[i][j] = max(dp[i][j],dp[i][j-i] + profit[i-1])

ans = 0

for i in range(n+1):
    ans = max(ans, max(dp[i]))
    
print(ans)

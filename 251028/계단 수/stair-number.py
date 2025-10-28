n = int(input())

# Please write your code here.
# dp[i][j] = i번째일 때, 마지막 숫자가 j일 때의 가지수

dp = [[0]*10 for _ in range(n+1)]

mod_num = 10**9 + 7
for i in range(1,10):
    dp[1][i] = 1

for i in range(2,n+1):
    for j in range(10):
        if j != 0:
            dp[i][j] += dp[i-1][j-1] %mod_num
        if j != 9:
            dp[i][j] += dp[i-1][j+1]% mod_num

# for d in dp:
#     print(d)

print(sum(dp[n])%mod_num)



n = int(input())

# Please write your code here.
# dp[i][j][k] = i일에 연속으로 B를 j번, T는 k번 받았을 때의 경우의 수

dp = [[[0]*3 for _ in range(3)] for _ in range(n+1)]

mod_num = 10**9 + 7

dp[1][0][0] = 1
dp[1][1][0] = 1
dp[1][0][1] = 1

for i in range(2, n+1):
    for j in range(3):
        for k in range(3):
            # G를 받았다면
            if j==0:
                dp[i][j][k] += (dp[i-1][0][k] + dp[i-1][1][k] + dp[i-1][2][k]) % mod_num
            # B를 받았다면
            if j!=0:
                dp[i][j][k] += dp[i-1][j-1][k] % mod_num
            # T를 받았다면
            if k!=0 and j == 0 :
                dp[i][j][k] += (dp[i-1][0][k-1] + dp[i-1][1][k-1] + dp[i-1][2][k-1])  % mod_num


# for d in dp:
#     for a in d:
#         print(a)
#     print()

ans = 0
for j in range(3):
    for k in range(3):
        ans += dp[n][j][k] % mod_num
print(ans)
N,K = map(int, input().split())
string = input()
string = " " + string
# Please write your code here.
# dp[i][j][k] = i번째 수정을 고려했을 때, j를 선택했을 때, k번 움직였을 때 최대 수정 개수 

import sys
MIN = -sys.maxsize

dp = [[[MIN]*(K+1) for _ in range(2)] for _ in range(N+1)]

dp[0][0][0] = 0


for i in range(1, N+1):
    for j in range(2):
        for k in range(K+1):
            # j=0
            if j == 0 :
                if k != 0:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][1][k-1])
                else: 
                    dp[i][j][k] = dp[i-1][j][k]
                if string[i] == "L":
                    dp[i][j][k] += 1 
            
            if j == 1:
                if k!=0:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][0][k-1])
                else: 
                    dp[i][j][k] = dp[i-1][j][k]
                if string[i] == "R":
                    dp[i][j][k] += 1

ans = 0 
for i in range(2):
    for j in range(K+1):
        ans = max(ans, dp[N][i][j])

print(ans)
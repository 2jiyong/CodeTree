n = int(input())
red = []
blue = []

for _ in range(2 * n):
    r, b = map(int, input().split())
    red.append(r)
    blue.append(b)

# Please write your code here.

# dp[i][j] = i번째 줄까지 고려햇을 때, 빨간 카드의 개수가 j 일 때 최대 값
import sys
MIN = -sys.maxsize

dp = [[MIN]*(n+1) for _ in range(2*n)] 


dp[0][0] = blue[0]
dp[0][1] = red[0]

for i in range(1, 2*n):
    for j in range(n+1):
        # red = 0 일 때 
        if j == 0:
            dp[i][j] = dp[i-1][j] + blue[i]
            continue
        if dp[i-1][j-1] != MIN:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + red[i])
        if dp[i-1][j] != MIN:
            dp[i][j] = max(dp[i][j], dp[i-1][j] + blue[i])


print(max(dp[2*n-1]))
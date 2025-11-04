n = int(input())
s = []
b = []
for _ in range(n):
    si, bi = map(int, input().split())
    s.append(si)
    b.append(bi)

# Please write your code here.
# dp[i][j][k] = i 번째 학생 고려했을 떄, 축구는 j명 야구는 k 명 뽑았을 때의 최대 점수
import sys
MIN = -sys.maxsize
dp = [[[MIN]*10 for _ in range(12)] for _ in range(n)]

dp[0][1][0] = s[0]
dp[0][0][1] = b[0]

for i in range(1, n):
    for j in range(12):
        for k in range(10):
            if j!= 0 and dp[i-1][j-1][k] != MIN:
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][k] + s[i])
            if k != 0 and dp[i-1][j][k-1] != MIN:
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1] + b[i])

# for d in dp[n-1]:
#     print(d)
print(dp[n-1][11][9])
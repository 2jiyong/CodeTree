N, M = map(int, input().split())
clothes = [tuple(map(int, input().split())) for _ in range(N)]
s = [x[0] for x in clothes]
e = [x[1] for x in clothes]
v = [x[2] for x in clothes]

# Please write your code here.
# dp[i][j] = i번째 일에, j라는 옷을 입었을 때의 최대점수

import sys 
MIN = - sys.maxsize

dp = [[MIN]*N for _ in range(M+1)]

for i in range(N):
    if s[i] == 1:
        dp[1][i] = 0

for i in range(2, M+1):
    for j in range(N):
        if s[j] > i or e[j] < i:
            continue

        for k in range(N): # 이전에 입은 거
            if dp[i-1][k] == MIN:
                continue
     
            dp[i][j] = max(dp[i][j], dp[i-1][k] + abs(v[j] - v[k]))

# for d in dp:
#     print(d)

print(max(dp[M]))

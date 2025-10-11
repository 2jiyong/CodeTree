N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)
# Please write your code here.
import sys
MIN = - sys.maxsize

dp = [MIN]* (M+1)
dp[0] = 0 


for i in range(N):
    for j in range(M,0,-1):
        if j<w[i]:
            continue
        if dp[j-w[i]] == MIN:
            continue
        dp[j] = max(dp[j], dp[j-w[i]] + v[i])
print(max(dp))



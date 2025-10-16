import sys
MAX = sys.maxsize

n, m = map(int, input().split())
quests = [tuple(map(int, input().split())) for _ in range(n)]

dp = [MAX] * (m + 1)
dp[0] = 0

for e, t in quests:
    for j in range(m, -1, -1):
        nxt = min(m, j + e)  # M 이상은 모두 M으로 처리
        dp[nxt] = min(dp[nxt], dp[j] + t)

print(-1 if dp[m] == MAX else dp[m])

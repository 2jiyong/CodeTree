n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

jobs.sort()
dp = [0]*n
# dp i 는 i 번 째 알바를 한다고 가정할 때 가장 많이 벌 수 있는 돈
for i in range(n):
    dp[i] = jobs[i][2]
    for j in range(i):
        if jobs[j][1] < jobs[i][0]:
            dp[i] = max(dp[i],dp[j] + jobs[i][2])

print(max(dp))

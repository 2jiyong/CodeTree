n = int(input())
values =[]
values.append((0,0,0))
for _ in range(n):
    value = tuple(map(int, input().split()))
    values.append(value)

# Please write your code here.
# dp[i][j] = i번째 층에서 j방을 들어갔을 때의 보물의 최대 개수

dp = [[0]*3 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(3):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j-2]) + values[i][j]
    

print(max(dp[n]))
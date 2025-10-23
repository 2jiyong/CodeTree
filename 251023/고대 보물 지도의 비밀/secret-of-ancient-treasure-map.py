n, k = map(int, input().split())
numbers = [0] + list(map(int, input().split()))

# Please write your code here.
# dp[i][j] = i번째를 선택했을 때, 음의 개수는 j일 때, 가장 큰 값
import sys 
MIN = -sys.maxsize
dp = [[MIN]*(k+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(1, n+1):
    for j in range(k+1):
        if numbers[i]>=0 and j==0:
            dp[i][j] = max(dp[i][j], numbers[i]) 
        if numbers[i]>=0:
            if dp[i-1][j] == MIN:
                continue
            dp[i][j] = dp[i-1][j] + numbers[i]
            continue
        if j == 0 :
            continue
        if dp[i-1][j-1] == MIN:
            continue
        dp[i][j] = dp[i-1][j-1] + numbers[i]

ans = 0 
for d in dp:
    ans = max(ans, max(d))
if ans == 0:
    ans = max(numbers[1:])
print(ans)
# 1. 음수일 때
# # j=0이면불가
# # dp[i-1][j-1] 에 더한다
# # 2. 양수일 때 선택하는 경우 
# 그 수로 시작하기 vs 그수로 끝내기
# 그 수로 시작하면 항상 음수의 개수는 0이다

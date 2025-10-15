n = int(input())
arr = list(map(int, input().split()))
arr.insert(0,0)
sum_nums = sum(arr)

# Please write your code here.
# dp[j][i] = i번째 수까지 고려했을 때, a,b의 차이가 j가 되는 최대합 
import sys
MIN = - sys.maxsize

dp = [[MIN] * (sum_nums+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(1,n+1):
    for j in range(sum_nums+1):
        # i를 추가 안했을 때
        dp[i][j] = max(dp[i][j],dp[i-1][j])

        if dp[i-1][abs(arr[i]-j)] != MIN:
            dp[i][j] = max(dp[i][j], dp[i-1][abs(arr[i]-j)] + arr[i])
 
        if arr[i]+j < sum_nums and dp[i-1][arr[i]+j] != MIN:
            dp[i][j] = max(dp[i][j], dp[i-1][arr[i]+j] + arr[i])

        # dp[i][j] = max(dp[i][j], dp[i-1][arr[i]+j] + arr[i])
        # 여기 뭔가 하나 추가 

print(dp[n][0]//2)
N, M = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
# dp[i][j] = i 까지 고려했을 때 합이 j인 경우의 가짓수

dp = [[0]*41 for _ in range(N)]
dp[0][nums[0]+20] +=1
dp[0][-nums[0]+20] +=1

# [20] = 0

for i in range(1,N):
    for j in range(41): # 0~40
        # i를 더하는 경우
        curr_num = j-20
        if curr_num-nums[i] >= -20 :
            dp[i][j] += dp[i-1][j-nums[i]]
        # i를 빼는 경우
        if curr_num+nums[i] <=20:
            dp[i][j] += dp[i-1][j+nums[i]]

# for d in dp:
#     print(d)
print(dp[N-1][M+20])

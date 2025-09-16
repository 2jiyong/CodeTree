MOD = 1000000007

# 변수 선언 및 입력:
n = int(input())

dp = [0] * (n + 1)

# 초기 조건 설정
dp[0] = 1
dp[1] = 2

for i in range(2,n+1):
    sum_num = 0 
    sum_num += dp[i-1] * 2 % MOD
    sum_num += dp[i-2] * 3 % MOD
    for j in range(i-3,-1,-1):
        sum_num += dp[j] * 2 % MOD
    dp[i] = sum_num % MOD

print(dp[n])


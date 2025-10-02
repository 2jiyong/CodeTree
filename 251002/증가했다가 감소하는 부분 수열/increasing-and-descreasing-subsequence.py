n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
dp = [0]*n

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if sequence[i] > sequence[j]:
            dp[i] = max(dp[i], dp[j] + 1)


def find_decrease_cnt(s_num):
    dp = [0]*n

    for i in range(n-1, s_num-1, -1):
        dp[i] = 1
        for j in range(n-1, i, -1):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

dp2 =[0]*n

for i in range(n):
    dp2[i] = dp[i]
    num = find_decrease_cnt(i)
    dp2[i] += num -1

print(max(dp2))
n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
dp = [0]*n
for i in range(n):
    for j in range(i):
        dist = i-j
        if dist<=arr[j]:
            if j != 0 and dp[j] == 0:
                continue 
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))


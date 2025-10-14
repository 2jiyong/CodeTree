n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
sum_nums = sum(arr)
target_num = sum_nums//2

dp = [[False] * (target_num+1) for _ in range(n)]

for i in range(n):
    # i 번째 수 고려중
    dp[i][arr[i]] = True
    if arr[i] > target_num:
        continue

    if i == 0:
        continue

    for j in range(1,target_num+1):
        # 합이 j가 되는 것이 가능?    
        # 이전에 가능했다면 이번도 가능
        if dp[i-1][j]:
            dp[i][j] = True
            continue
            
        if j < arr[i]:
            continue
        # 이전에 불가했다면?
        # 직접 체크
        if dp[i-1][j-arr[i]]:
            dp[i][j] = True
            continue


import sys

for j in range(target_num,-1,-1):
    if dp[n-1][j]:
        print(sum_nums-j-j)
        sys.exit()

# for d in dp:
#     print(d)      
        


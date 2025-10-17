n = int(input())
arr = list(map(int, input().split()))
arr.insert(0,0)
sum_nums = sum(arr)

# Please write your code here.
# dp[i] 는 합이 i가 가능한지 여부
dp = [False] * (sum_nums+1)
dp[0] = True

for i in range(1,n+1):
    for j in range(sum_nums,-1,-1):
        if arr[i] > j:
            continue
        
        if dp[j-arr[i]]:
            dp[j] = True

tar_num = sum_nums//2

if dp[tar_num] and sum_nums%2 == 0 :
    print("Yes")
else: 
    print("No")
        
        
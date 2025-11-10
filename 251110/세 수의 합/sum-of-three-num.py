n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
d = dict()

for num in arr:
    if num in d:
        d[num] += 1
    else:
        d[num] = 1

ans = 0
for i in range(n):
    target_num1 = k-arr[i]
    d[arr[i]] -= 1
    for j in range(i):
        target_num2 = target_num1 - arr[j]
        if target_num2 in d:
            ans+= d[target_num2]

print(ans)
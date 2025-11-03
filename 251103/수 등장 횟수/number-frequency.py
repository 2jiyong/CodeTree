n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

# Please write your code here.

d = {}

for num in arr:
    if num not in d:
        d[num] = 1
    else:
        d[num] += 1

for num in nums:
    if num not in d:
        print(0, end=" ")
    else:
        print(d[num], end= " ")
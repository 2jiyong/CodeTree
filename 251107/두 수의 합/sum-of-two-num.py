n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
d = dict()
for num in arr:
    if num not in d:
        d[num] = 1
    else:
        d[num] +=1

ans = 0 

for num in arr:
    target = k-num
    if target in d:
        ans += d[target]
        if target == num :
            ans -= 1 

print(ans//2)

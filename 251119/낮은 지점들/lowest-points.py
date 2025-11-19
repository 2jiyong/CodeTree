n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
d = dict()
ans = 0 
for x,y in points:
    if x in d:
        d[x] = min(d[x], y)
    else:
        d[x] = y

ans = 0
for k, v in d.items():
    ans += v
print(ans)
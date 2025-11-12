n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
d = dict()
for num in arr:
    if num in d:
        d[num] +=1
    else:
        d[num] = 1


items = []

for num, cnt in d.items():
    item = [num,cnt]
    items.append(item)

items.sort(key=lambda x:(-x[1],-x[0]))

if len(items)<=k:
    for item in items:
        print(item[0], end=" ")
else:
    for i in range(k):
        print(items[i][0], end=" ")
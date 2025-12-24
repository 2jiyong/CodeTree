n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
from sortedcontainers import SortedDict

sd = SortedDict()

for i in range(n):
    num = arr[i]
    if num in sd:
        continue
    else:
        sd[num] = i + 1

for k,v in sd.items():
    print(k,v)
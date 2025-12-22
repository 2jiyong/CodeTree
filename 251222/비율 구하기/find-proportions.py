n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.
from sortedcontainers import SortedDict

sd = SortedDict()

for word in words:
    if word in sd:
        sd[word] += 1
    else:
        sd[word] = 1

for key, value in sd.items():
    print(key, end=" ")
    print(f"{value/n*100:.4f}")
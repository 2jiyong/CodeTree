n = int(input())
words = [''.join(sorted(input())) for _ in range(n)]

# Please write your code here.
d = dict()
for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
ans = 0 
for v in d.values():
    ans = max(ans,v)
print(ans)
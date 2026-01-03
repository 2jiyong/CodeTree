n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
ans = n+m
for a in A: 
    if a in B:
        ans -= 2
print(ans)
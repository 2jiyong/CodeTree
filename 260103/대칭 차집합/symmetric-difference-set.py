n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
b = set(B)

ans = n+m
for a in A:
    if a in b:
        ans -= 2 
print(ans)
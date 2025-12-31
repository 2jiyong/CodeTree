n, m = map(int, input().split())

A = [input() for _ in range(n)]
B = [input() for _ in range(n)]

# Please write your code here.
ans = 0
for i in range(m):
    for j in range(i+1,m):
        for k in range(j+1,m):
            s = set()
            for a in A:
                string = a[i]+a[j]+a[k]
                s.add(string)

            is_seperated = True
            for b in B:
                string = b[i]+b[j]+b[k]
                if string in s:
                    is_seperated = False
            if is_seperated:
                ans +=1
                
print(ans)
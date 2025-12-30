n, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
people = [0] + [num for num in range(1,n+1)]

sits = [0]+[{i} for i in range(1,n+1)]

for i in range(3):
    for j in range(k):
        a = edges[j][0]
        b = edges[j][1]
        p1 = people[a]
        p2 = people[b]
        sits[p1].add(b)
        sits[p2].add(a)
        people[a], people[b] = people[b], people[a]

for i in range(1,n+1):
    print(len(sits[i]))
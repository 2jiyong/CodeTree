n = int(input())
values = []
values.append((0,0,0))
for _ in range(n):
    value = tuple(map(int, input().split()))
    values.append(value)

# Please write your code here.
# dp[i][j] = i번 째 층, j 방
dp = [[0]*(3) for _ in range(n+1)]

ans = 0 

def initialize(first_room):
    global dp
    dp = [[0]*(3) for _ in range(n+1)]
    dp[1][first_room] = values[1][first_room]

for first_room in range(3):
    initialize(first_room)
    for i in range(2,n):
        for j in range(3):
            dp[i][j] = max(dp[i-1][j-2], dp[i-1][j-1]) + values[i][j]
    # print(dp)
    # 고쳐야 함 
    # n번 방에 들어갔다면, 마지막엔 n-1번, n-2번 방으로 갈 수 있음
    # n-1번 방으로 가는경우는 n-2번, n번 방의 최대, n-2번 방으로 가는 경우엔 n번, n-1번 방의 최대

    # n-1번 방일 때  
    ans = max(ans, max(dp[n-1][first_room-2], dp[n-1][first_room])+values[n][first_room-1])
    # n-2번 방일 때 
    ans = max(ans, max(dp[n-1][first_room], dp[n-1][first_room-1])+values[n][first_room-2])

    # print(ans)

print(ans)
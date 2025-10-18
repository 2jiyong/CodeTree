# Variable declaration and input:
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
dp = [
    [-1] * n
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# Starting from (x, y), find the maximum number of cells
# that can be reached while satisfying the conditions.
def find_max(x, y):
    # If it has already been calculated,
    # return that value immediately.
    if dp[x][y] != -1:
        return dp[x][y]

    # The default value is itself.
    best = 1

    # Look at cells in order of increasing integer value
    # and calculate the optimal number of cells for 4 directions.
    dxs = [-1, 1,  0, 0]
    dys = [ 0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] > grid[x][y]:
            best = max(best, find_max(nx, ny) + 1)

    dp[x][y] = best
    return dp[x][y]


# Update the maximum number of cells that can be moved
# starting from each cell.
ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, find_max(i, j))

print(ans)

from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

grid = []
target = None

for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
    for j in range(m):
        if row[j] == 2:
            target = (i, j)

result = [[-1] * m for _ in range(n)]

queue = deque([target])
result[target[0]][target[1]] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    y, x = queue.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m:
            if result[ny][nx] == -1 and grid[ny][nx] == 1:
                result[ny][nx] = result[y][x] + 1
                queue.append((ny, nx))

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            result[i][j] = 0

for row in result:
    print(" ".join(map(str, row)))

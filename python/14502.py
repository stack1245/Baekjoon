from collections import deque
from itertools import combinations

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

empty = []
virus = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            empty.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))


def spread():
    temp = [row[:] for row in lab]
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                q.append((nx, ny))
    return sum(row.count(0) for row in temp)


ans = 0
for walls in combinations(empty, 3):
    for x, y in walls:
        lab[x][y] = 1
    ans = max(ans, spread())
    for x, y in walls:
        lab[x][y] = 0

print(ans)

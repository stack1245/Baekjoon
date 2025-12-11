from collections import deque

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            sx, sy = i, j
            space[i][j] = 0

size = 2
ate = 0
time = 0


def bfs(x, y):
    visited = [[False] * n for _ in range(n)]
    q = deque([(x, y, 0)])
    visited[x][y] = True
    candidates = []

    while q:
        cx, cy, dist = q.popleft()

        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if space[nx][ny] <= size:
                    visited[nx][ny] = True
                    if 0 < space[nx][ny] < size:
                        candidates.append((dist + 1, nx, ny))
                    q.append((nx, ny, dist + 1))

    if not candidates:
        return None
    candidates.sort()
    return candidates[0]


while True:
    result = bfs(sx, sy)
    if not result:
        break

    dist, fx, fy = result
    time += dist
    ate += 1
    if ate == size:
        size += 1
        ate = 0

    space[fx][fy] = 0
    sx, sy = fx, fy

print(time)

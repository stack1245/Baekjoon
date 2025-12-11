from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


def find_air():
    air = [[0] * m for _ in range(n)]
    q = deque([(0, 0)])
    air[0][0] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not air[nx][ny] and grid[nx][ny] == 0:
                air[nx][ny] = 1
                q.append((nx, ny))
    return air


time = 0
while True:
    air = find_air()
    melt = []

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                cnt = 0
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and air[ni][nj]:
                        cnt += 1
                if cnt >= 2:
                    melt.append((i, j))

    if not melt:
        break

    for x, y in melt:
        grid[x][y] = 0
    time += 1

print(time)

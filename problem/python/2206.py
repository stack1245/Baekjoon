from collections import deque

n, m = map(int, input().split())
grid = [input() for _ in range(n)]

q = deque([(0, 0, 0, 1)])
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

while q:
    x, y, broken, dist = q.popleft()

    if x == n - 1 and y == m - 1:
        print(dist)
        exit()

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if grid[nx][ny] == "0" and not visited[nx][ny][broken]:
                visited[nx][ny][broken] = 1
                q.append((nx, ny, broken, dist + 1))
            elif grid[nx][ny] == "1" and broken == 0 and not visited[nx][ny][1]:
                visited[nx][ny][1] = 1
                q.append((nx, ny, 1, dist + 1))

print(-1)

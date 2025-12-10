from collections import deque

n, m = map(int, input().split())
maze = [list(input()) for _ in range(n)]

queue = deque([(0, 0, 1)])
visited = [[False] * m for _ in range(n)]
visited[0][0] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y, dist = queue.popleft()

    if x == n - 1 and y == m - 1:
        print(dist)
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maze[nx][ny] == "1":
            visited[nx][ny] = True
            queue.append((nx, ny, dist + 1))

from collections import deque

n = int(input())
grid = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, visited, is_colorblind):
    queue = deque([(x, y)])
    visited[x][y] = True
    color = grid[x][y]

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if is_colorblind:
                    if (color in "RG" and grid[nx][ny] in "RG") or (
                        color == grid[nx][ny]
                    ):
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                else:
                    if color == grid[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))


visited1 = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]
count1 = 0
count2 = 0

for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            bfs(i, j, visited1, False)
            count1 += 1
        if not visited2[i][j]:
            bfs(i, j, visited2, True)
            count2 += 1

print(count1, count2)

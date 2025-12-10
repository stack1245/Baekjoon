from collections import deque

n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
complexes = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 1

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if (
                0 <= nx < n
                and 0 <= ny < n
                and not visited[nx][ny]
                and graph[nx][ny] == "1"
            ):
                visited[nx][ny] = True
                queue.append((nx, ny))
                count += 1

    return count


for i in range(n):
    for j in range(n):
        if graph[i][j] == "1" and not visited[i][j]:
            complexes.append(bfs(i, j))

complexes.sort()
print(len(complexes))
for c in complexes:
    print(c)

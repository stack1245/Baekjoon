from collections import deque

n, m = map(int, input().split())
campus = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            start = (i, j)
            break

queue = deque([start])
visited = [[False] * m for _ in range(n)]
visited[start[0]][start[1]] = True
count = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if campus[nx][ny] != 'X':
                visited[nx][ny] = True
                queue.append((nx, ny))
                if campus[nx][ny] == 'P':
                    count += 1

print(count if count > 0 else 'TT')

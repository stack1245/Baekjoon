import sys
from collections import deque

input = sys.stdin.readline


def bfs(field, M, N, x, y):
    queue = deque([(x, y)])
    field[y][x] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < M and 0 <= ny < N and field[ny][nx] == 1:
                field[ny][nx] = 0
                queue.append((nx, ny))


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    field = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    count = 0
    for y in range(N):
        for x in range(M):
            if field[y][x] == 1:
                bfs(field, M, N, x, y)
                count += 1

    print(count)

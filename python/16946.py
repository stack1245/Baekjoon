import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

group = [[0] * M for _ in range(N)]
group_size = {}
group_id = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if board[i][j] == "0" and group[i][j] == 0:
            q = deque([(i, j)])
            group[i][j] = group_id
            cnt = 1

            while q:
                x, y = q.popleft()
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if (
                        0 <= nx < N
                        and 0 <= ny < M
                        and board[nx][ny] == "0"
                        and group[nx][ny] == 0
                    ):
                        group[nx][ny] = group_id
                        q.append((nx, ny))
                        cnt += 1

            group_size[group_id] = cnt
            group_id += 1

result = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == "1":
            cnt = 1
            adjacent = set()
            for d in range(4):
                ni, nj = i + dx[d], j + dy[d]
                if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == "0":
                    adjacent.add(group[ni][nj])

            for gid in adjacent:
                cnt += group_size[gid]

            result[i][j] = cnt % 10

for row in result:
    print("".join(map(str, row)))

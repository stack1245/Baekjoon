from collections import deque
import sys

input = sys.stdin.readline


def solve():
    h, w = map(int, input().split())
    board = [list(input().strip()) for _ in range(h)]
    keys = set(input().strip())
    if "0" in keys:
        keys = set()

    visited = [[False] * w for _ in range(h)]
    doors = {chr(ord("A") + i): [] for i in range(26)}
    q = deque()

    for i in range(h):
        for j in range(w):
            if i == 0 or i == h - 1 or j == 0 or j == w - 1:
                if board[i][j] != "*":
                    q.append((i, j))
                    visited[i][j] = True

    count = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        c = board[x][y]

        if c == "$":
            count += 1
            board[x][y] = "."
        elif c.isupper():
            if c.lower() not in keys:
                doors[c].append((x, y))
                continue
        elif c.islower():
            if c not in keys:
                keys.add(c)
                if doors[c.upper()]:
                    for dx2, dy2 in doors[c.upper()]:
                        q.append((dx2, dy2))
                    doors[c.upper()] = []

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (
                0 <= nx < h
                and 0 <= ny < w
                and not visited[nx][ny]
                and board[nx][ny] != "*"
            ):
                visited[nx][ny] = True
                q.append((nx, ny))

    print(count)


t = int(input())
for _ in range(t):
    solve()

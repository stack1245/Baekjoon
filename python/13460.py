from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == "R":
            rx, ry = i, j
            board[i][j] = "."
        elif board[i][j] == "B":
            bx, by = i, j
            board[i][j] = "."


def move(x, y, dx, dy):
    cnt = 0
    while board[x + dx][y + dy] != "#" and board[x][y] != "O":
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt


q = deque([(rx, ry, bx, by, 0)])
visited = set([(rx, ry, bx, by)])
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    rx, ry, bx, by, depth = q.popleft()

    if depth >= 10:
        break

    for dx, dy in directions:
        nrx, nry, rcnt = move(rx, ry, dx, dy)
        nbx, nby, bcnt = move(bx, by, dx, dy)

        if board[nbx][nby] == "O":
            continue

        if board[nrx][nry] == "O":
            print(depth + 1)
            sys.exit()

        if nrx == nbx and nry == nby:
            if rcnt > bcnt:
                nrx -= dx
                nry -= dy
            else:
                nbx -= dx
                nby -= dy

        if (nrx, nry, nbx, nby) not in visited:
            visited.add((nrx, nry, nbx, nby))
            q.append((nrx, nry, nbx, nby, depth + 1))

print(-1)

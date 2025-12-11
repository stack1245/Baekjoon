import sys

input = sys.stdin.readline

r, c = map(int, input().split())
board = [input().strip() for _ in range(r)]

ans = 1


def dfs(x, y, cnt, visited):
    global ans
    ans = max(ans, cnt)

    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c:
            idx = ord(board[nx][ny]) - ord("A")
            if not (visited & (1 << idx)):
                dfs(nx, ny, cnt + 1, visited | (1 << idx))


start_idx = ord(board[0][0]) - ord("A")
dfs(0, 0, 1, 1 << start_idx)
print(ans)

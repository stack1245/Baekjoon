import sys

sys.setrecursionlimit(1000001)
input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

parent = list(range(N * M))


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x


direction = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

for i in range(N):
    for j in range(M):
        di, dj = direction[board[i][j]]
        ni, nj = i + di, j + dj
        union(i * M + j, ni * M + nj)

print(len(set(find(i) for i in range(N * M))))

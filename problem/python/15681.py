import sys

sys.setrecursionlimit(200000)
input = sys.stdin.readline

n, r, q = map(int, input().split())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

size = [0] * (n + 1)


def dfs(node, parent):
    size[node] = 1
    for child in tree[node]:
        if child != parent:
            size[node] += dfs(child, node)
    return size[node]


dfs(r, -1)

for _ in range(q):
    print(size[int(input())])

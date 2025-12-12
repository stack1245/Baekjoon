import sys

input = sys.stdin.readline


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, rank, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x == y:
        return False

    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[y] = x
        rank[x] += 1

    return True


n, m = map(int, input().split())
edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)

total = 0
max_edge = 0
edge_count = 0

for cost, a, b in edges:
    if union(parent, rank, a, b):
        total += cost
        max_edge = max(max_edge, cost)
        edge_count += 1
        if edge_count == n - 1:
            break

print(total - max_edge)

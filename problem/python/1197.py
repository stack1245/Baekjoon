v, e = map(int, input().split())
parent = list(range(v + 1))


def find(x):
    root = x
    while parent[root] != root:
        root = parent[root]
    while parent[x] != root:
        parent[x], x = root, parent[x]
    return root


def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        parent[y] = x


edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

total = 0
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        total += cost

print(total)

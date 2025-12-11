def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
planets = []
for i in range(n):
    x, y, z = map(int, input().split())
    planets.append((x, y, z, i))

edges = []
for j in range(3):
    planets.sort(key=lambda p: p[j])
    for i in range(n - 1):
        cost = abs(planets[i][j] - planets[i + 1][j])
        edges.append((cost, planets[i][3], planets[i + 1][3]))

edges.sort()
parent = list(range(n))

ans = 0
cnt = 0
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        ans += cost
        cnt += 1
        if cnt == n - 1:
            break

print(ans)

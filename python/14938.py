n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
INF = 10**9
d = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    d[i][i] = 0

for _ in range(r):
    a, b, c = map(int, input().split())
    d[a][b] = d[b][a] = c

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

ans = 0
for i in range(1, n + 1):
    total = sum(items[j] for j in range(1, n + 1) if d[i][j] <= m)
    ans = max(ans, total)

print(ans)

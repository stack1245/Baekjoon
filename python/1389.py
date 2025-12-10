n, m = map(int, input().split())
INF = float("inf")
dist = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dist[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    dist[a][b] = 1
    dist[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

min_bacon = INF
result = 0

for i in range(1, n + 1):
    bacon = sum(dist[i][1:])
    if bacon < min_bacon:
        min_bacon = bacon
        result = i

print(result)

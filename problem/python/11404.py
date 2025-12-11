n = int(input())
m = int(input())
INF = 10**9
d = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    d[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    d[a][b] = min(d[a][b], c)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(d[i][j] if d[i][j] != INF else 0, end=" ")
    print()

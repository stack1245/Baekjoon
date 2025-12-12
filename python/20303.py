import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
candy = [0] + list(map(int, input().split()))

parent = list(range(N + 1))


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x


for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

groups = {}
for i in range(1, N + 1):
    root = find(i)
    if root not in groups:
        groups[root] = [0, 0]
    groups[root][0] += 1
    groups[root][1] += candy[i]

items = list(groups.values())
dp = [0] * K

for cnt, total in items:
    for j in range(K - 1, cnt - 1, -1):
        dp[j] = max(dp[j], dp[j - cnt] + total)

print(dp[K - 1])

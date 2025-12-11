import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline


def dfs(graph, v, visited):
    visited[v] = True

    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(graph, next_v, visited)


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)
count = 0

for i in range(1, N + 1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1

print(count)

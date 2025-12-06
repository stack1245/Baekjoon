from collections import deque
import sys

input = sys.stdin.readline


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    for next_v in sorted(graph[v]):
        if not visited[next_v]:
            dfs(graph, next_v, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for next_v in sorted(graph[v]):
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)


N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
dfs(graph, V, visited)
print()

visited = [False] * (N + 1)
bfs(graph, V, visited)
print()

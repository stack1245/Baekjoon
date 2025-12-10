from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n + 1)
visited = [False] * (n + 1)

q = deque([1])
visited[1] = True

while q:
    node = q.popleft()
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            parent[next_node] = node
            q.append(next_node)

for i in range(2, n + 1):
    print(parent[i])

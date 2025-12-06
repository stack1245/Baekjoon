def dfs(graph, start, visited):
    visited[start] = True
    count = 0

    for neighbor in graph[start]:
        if not visited[neighbor]:
            count += 1 + dfs(graph, neighbor, visited)

    return count


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = dfs(graph, 1, visited)
print(result)

import heapq

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

start, end = map(int, input().split())

dist = [float("inf")] * (n + 1)
prev = [0] * (n + 1)
dist[start] = 0

pq = [(0, start)]
while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for cost, v in graph[u]:
        if dist[u] + cost < dist[v]:
            dist[v] = dist[u] + cost
            prev[v] = u
            heapq.heappush(pq, (dist[v], v))

path = []
node = end
while node:
    path.append(node)
    node = prev[node]
path.reverse()

print(dist[end])
print(len(path))
print(*path)

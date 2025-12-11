import heapq
import sys

input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dist = [float("inf")] * (v + 1)
dist[k] = 0

q = [(0, k)]

while q:
    d, now = heapq.heappop(q)

    if dist[now] < d:
        continue

    for next_node, cost in graph[now]:
        new_cost = d + cost
        if new_cost < dist[next_node]:
            dist[next_node] = new_cost
            heapq.heappush(q, (new_cost, next_node))

for i in range(1, v + 1):
    if dist[i] == float("inf"):
        print("INF")
    else:
        print(dist[i])

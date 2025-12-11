import heapq
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

dist = [float("inf")] * (n + 1)
dist[start] = 0

q = [(0, start)]

while q:
    d, now = heapq.heappop(q)

    if dist[now] < d:
        continue

    for next_node, cost in graph[now]:
        new_cost = d + cost
        if new_cost < dist[next_node]:
            dist[next_node] = new_cost
            heapq.heappush(q, (new_cost, next_node))

print(dist[end])

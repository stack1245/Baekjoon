import heapq
import sys

input = sys.stdin.readline
INF = float("inf")


def dijkstra(start):
    dist = [INF] * (n + 1)
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

    return dist


n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

dist_1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

path1 = dist_1[v1] + dist_v1[v2] + dist_v2[n]
path2 = dist_1[v2] + dist_v2[v1] + dist_v1[n]

result = min(path1, path2)

if result >= INF:
    print(-1)
else:
    print(result)

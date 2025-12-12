import heapq

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
rev_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((t, b))
    rev_graph[b].append((t, a))


def dijkstra(g, start):
    dist = [float("inf")] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for cost, v in g[u]:
            if dist[u] + cost < dist[v]:
                dist[v] = dist[u] + cost
                heapq.heappush(pq, (dist[v], v))
    return dist


go = dijkstra(graph, x)
back = dijkstra(rev_graph, x)

print(max(go[i] + back[i] for i in range(1, n + 1)))

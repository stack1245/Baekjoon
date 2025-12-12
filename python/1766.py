import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

heap = []
for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

result = []
while heap:
    node = heapq.heappop(heap)
    result.append(node)
    for nxt in graph[node]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(heap, nxt)

print(*result)

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    data = list(map(int, input().split()))
    cnt = data[0]
    for i in range(1, cnt):
        graph[data[i]].append(data[i + 1])
        indegree[data[i + 1]] += 1

q = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

result = []
while q:
    node = q.popleft()
    result.append(node)
    for nxt in graph[node]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

if len(result) == N:
    for r in result:
        print(r)
else:
    print(0)

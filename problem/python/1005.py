import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    w = int(input())

    queue = deque()
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = time[i]

    while queue:
        node = queue.popleft()

        for next_node in graph[node]:
            dp[next_node] = max(dp[next_node], dp[node] + time[next_node])
            indegree[next_node] -= 1

            if indegree[next_node] == 0:
                queue.append(next_node)

    print(dp[w])

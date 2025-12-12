import sys

sys.setrecursionlimit(111111)
input = sys.stdin.readline


def dfs(node):
    visited[node] = True
    cycle.append(node)
    nxt = graph[node]

    if visited[nxt]:
        if nxt in cycle:
            idx = cycle.index(nxt)
            return len(cycle) - idx
        return 0
    else:
        return dfs(nxt)


T = int(input())
for _ in range(T):
    n = int(input())
    graph = [0] + list(map(int, input().split()))

    visited = [False] * (n + 1)
    cnt = 0

    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            cnt += dfs(i)

    print(n - cnt)

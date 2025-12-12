import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(0)
    exit()

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dfs(node, parent, dist):
    max_dist = dist
    farthest = node

    for next_node, cost in graph[node]:
        if next_node != parent:
            d, f = dfs(next_node, node, dist + cost)
            if d > max_dist:
                max_dist = d
                farthest = f

    return max_dist, farthest


_, far_node = dfs(1, -1, 0)
diameter, _ = dfs(far_node, -1, 0)

print(diameter)

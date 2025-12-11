from collections import deque

v = int(input())
tree = [[] for _ in range(v + 1)]

for _ in range(v):
    data = list(map(int, input().split()))
    node = data[0]
    i = 1
    while data[i] != -1:
        tree[node].append((data[i], data[i + 1]))
        i += 2


def bfs(start):
    visited = [-1] * (v + 1)
    visited[start] = 0
    q = deque([start])

    while q:
        node = q.popleft()
        for next_node, dist in tree[node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[node] + dist
                q.append(next_node)

    max_dist = max(visited)
    max_node = visited.index(max_dist)
    return max_node, max_dist


node, _ = bfs(1)
_, diameter = bfs(node)
print(diameter)

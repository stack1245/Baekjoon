from collections import deque

n, k = map(int, input().split())

dist = [-1] * 100001
dist[n] = 0

q = deque([n])

while q:
    x = q.popleft()

    if x == k:
        print(dist[k])
        break

    if x * 2 <= 100000 and dist[x * 2] == -1:
        dist[x * 2] = dist[x]
        q.appendleft(x * 2)

    if x - 1 >= 0 and dist[x - 1] == -1:
        dist[x - 1] = dist[x] + 1
        q.append(x - 1)

    if x + 1 <= 100000 and dist[x + 1] == -1:
        dist[x + 1] = dist[x] + 1
        q.append(x + 1)

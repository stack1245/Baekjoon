from collections import deque

n, k = map(int, input().split())
if n >= k:
    print(n - k)
    print(1)
else:
    visited = [-1] * 100001
    cnt = [0] * 100001
    q = deque([n])
    visited[n] = 0
    cnt[n] = 1

    while q:
        x = q.popleft()
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= 100000:
                if visited[nx] == -1:
                    visited[nx] = visited[x] + 1
                    cnt[nx] = cnt[x]
                    q.append(nx)
                elif visited[nx] == visited[x] + 1:
                    cnt[nx] += cnt[x]

    print(visited[k])
    print(cnt[k])

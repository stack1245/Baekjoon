import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    if a == b:
        print()
        continue

    queue = deque([(a, "")])
    visited = [False] * 10000
    visited[a] = True

    while queue:
        num, path = queue.popleft()

        d = (num * 2) % 10000
        if d == b:
            print(path + "D")
            break
        if not visited[d]:
            visited[d] = True
            queue.append((d, path + "D"))

        s = (num - 1) % 10000
        if s == b:
            print(path + "S")
            break
        if not visited[s]:
            visited[s] = True
            queue.append((s, path + "S"))

        l = (num % 1000) * 10 + num // 1000
        if l == b:
            print(path + "L")
            break
        if not visited[l]:
            visited[l] = True
            queue.append((l, path + "L"))

        r = (num % 10) * 1000 + num // 10
        if r == b:
            print(path + "R")
            break
        if not visited[r]:
            visited[r] = True
            queue.append((r, path + "R"))

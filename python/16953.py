from collections import deque

a, b = map(int, input().split())

q = deque([(a, 1)])
visited = set([a])

while q:
    num, count = q.popleft()

    if num == b:
        print(count)
        exit()

    for next_num in [num * 2, num * 10 + 1]:
        if next_num <= b and next_num not in visited:
            visited.add(next_num)
            q.append((next_num, count + 1))

print(-1)

from collections import deque

N, K = map(int, input().split())

if N == K:
    print(0)
else:
    visited = [False] * 100001
    queue = deque([(N, 0)])
    visited[N] = True

    while queue:
        pos, time = queue.popleft()

        next_positions = [pos - 1, pos + 1, pos * 2]

        for next_pos in next_positions:
            if next_pos == K:
                print(time + 1)
                exit()

            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))

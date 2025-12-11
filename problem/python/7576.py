from collections import deque
import sys

input = sys.stdin.readline

M, N = map(int, input().split())

box = []
queue = deque()

for n in range(N):
    row = list(map(int, input().split()))
    box.append(row)
    for m in range(M):
        if row[m] == 1:
            queue.append((n, m))

dn = [-1, 1, 0, 0]
dm = [0, 0, -1, 1]

while queue:
    n, m = queue.popleft()

    for i in range(4):
        nn = n + dn[i]
        nm = m + dm[i]

        if 0 <= nn < N and 0 <= nm < M:
            if box[nn][nm] == 0:
                box[nn][nm] = box[n][m] + 1
                queue.append((nn, nm))

max_days = 0
for n in range(N):
    for m in range(M):
        if box[n][m] == 0:
            print(-1)
            exit()
        max_days = max(max_days, box[n][m])

print(max_days - 1)

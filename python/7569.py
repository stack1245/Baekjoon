from collections import deque
import sys

input = sys.stdin.readline

M, N, H = map(int, input().split())

box = []
queue = deque()

for h in range(H):
    layer = []
    for n in range(N):
        row = list(map(int, input().split()))
        layer.append(row)
        for m in range(M):
            if row[m] == 1:
                queue.append((h, n, m))
    box.append(layer)

dh = [-1, 1, 0, 0, 0, 0]
dn = [0, 0, -1, 1, 0, 0]
dm = [0, 0, 0, 0, -1, 1]

while queue:
    h, n, m = queue.popleft()

    for i in range(6):
        nh = h + dh[i]
        nn = n + dn[i]
        nm = m + dm[i]

        if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M:
            if box[nh][nn][nm] == 0:
                box[nh][nn][nm] = box[h][n][m] + 1
                queue.append((nh, nn, nm))

max_days = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 0:
                print(-1)
                exit()
            max_days = max(max_days, box[h][n][m])

print(max_days - 1)

r, c, t = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]

cleaner = []
for i in range(r):
    if a[i][0] == -1:
        cleaner.append(i)


def spread():
    temp = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if a[i][j] > 0:
                cnt = 0
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < r and 0 <= nj < c and a[ni][nj] != -1:
                        temp[ni][nj] += a[i][j] // 5
                        cnt += 1
                temp[i][j] += a[i][j] - (a[i][j] // 5) * cnt
    for i in range(r):
        for j in range(c):
            if a[i][j] != -1:
                a[i][j] = temp[i][j]


def clean():
    top, bot = cleaner

    for i in range(top - 1, 0, -1):
        a[i][0] = a[i - 1][0]
    for j in range(c - 1):
        a[0][j] = a[0][j + 1]
    for i in range(top):
        a[i][c - 1] = a[i + 1][c - 1]
    for j in range(c - 1, 1, -1):
        a[top][j] = a[top][j - 1]
    a[top][1] = 0

    for i in range(bot + 1, r - 1):
        a[i][0] = a[i + 1][0]
    for j in range(c - 1):
        a[r - 1][j] = a[r - 1][j + 1]
    for i in range(r - 1, bot, -1):
        a[i][c - 1] = a[i - 1][c - 1]
    for j in range(c - 1, 1, -1):
        a[bot][j] = a[bot][j - 1]
    a[bot][1] = 0


for _ in range(t):
    spread()
    clean()

print(sum(sum(row) for row in a) + 2)

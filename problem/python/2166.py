n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

area = 0
for i in range(n):
    area += points[i][0] * points[(i + 1) % n][1]
    area -= points[(i + 1) % n][0] * points[i][1]

print(abs(area) / 2)

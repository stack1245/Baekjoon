from itertools import combinations

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

houses = []
chickens = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

answer = float("inf")

for selected in combinations(chickens, m):
    total = 0
    for hx, hy in houses:
        min_dist = float("inf")
        for cx, cy in selected:
            min_dist = min(min_dist, abs(hx - cx) + abs(hy - cy))
        total += min_dist
    answer = min(answer, total)

print(answer)

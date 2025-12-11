def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)


def intersect(l1, l2):
    x1, y1, x2, y2 = l1
    x3, y3, x4, y4 = l2

    abc = ccw(x1, y1, x2, y2, x3, y3)
    abd = ccw(x1, y1, x2, y2, x4, y4)
    cda = ccw(x3, y3, x4, y4, x1, y1)
    cdb = ccw(x3, y3, x4, y4, x2, y2)

    if abc * abd == 0 and cda * cdb == 0:
        return (
            min(x1, x2) <= max(x3, x4)
            and min(x3, x4) <= max(x1, x2)
            and min(y1, y2) <= max(y3, y4)
            and min(y3, y4) <= max(y1, y2)
        )

    return abc * abd <= 0 and cda * cdb <= 0


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a


n = int(input())
lines = []
for _ in range(n):
    lines.append(list(map(int, input().split())))

parent = list(range(n))

for i in range(n):
    for j in range(i + 1, n):
        if intersect(lines[i], lines[j]):
            union(i, j)

groups = {}
for i in range(n):
    root = find(i)
    groups[root] = groups.get(root, 0) + 1

print(len(groups))
print(max(groups.values()))

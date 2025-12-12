import sys

input = sys.stdin.readline


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, rank, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x == y:
        return False

    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[y] = x
        rank[x] += 1

    return True


n, m = map(int, input().split())
parent = [i for i in range(n)]
rank = [0] * n

for i in range(1, m + 1):
    a, b = map(int, input().split())
    if not union(parent, rank, a, b):
        print(i)
        break
else:
    print(0)

import sys
import bisect

input = sys.stdin.readline


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    parent[x] = y


N, M, K = map(int, input().split())
cards = list(map(int, input().split()))
cheolsu = list(map(int, input().split()))

cards.sort()

parent = list(range(M))

result = []

for c in cheolsu:
    idx = bisect.bisect_right(cards, c)

    idx = find(parent, idx)

    result.append(cards[idx])

    if idx + 1 < M:
        union(parent, idx, idx + 1)

for r in result:
    print(r)

import sys

sys.setrecursionlimit(200000)
input = sys.stdin.readline

G = int(input())
P = int(input())

parent = list(range(G + 1))


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


ans = 0
for _ in range(P):
    g = int(input())
    gate = find(g)

    if gate == 0:
        break

    parent[gate] = gate - 1
    ans += 1

print(ans)

import sys

input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

subA = {}
for i in range(n):
    s = 0
    for j in range(i, n):
        s += A[j]
        subA[s] = subA.get(s, 0) + 1

ans = 0
for i in range(m):
    s = 0
    for j in range(i, m):
        s += B[j]
        if T - s in subA:
            ans += subA[T - s]

print(ans)

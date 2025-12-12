import sys

input = sys.stdin.readline

n = int(input())
A, B, C, D = [], [], [], []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = {}
for a in A:
    for b in B:
        s = a + b
        AB[s] = AB.get(s, 0) + 1

ans = 0
for c in C:
    for d in D:
        s = c + d
        if -s in AB:
            ans += AB[-s]

print(ans)

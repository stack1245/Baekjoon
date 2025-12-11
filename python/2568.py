import bisect

n = int(input())
lines = []
for _ in range(n):
    a, b = map(int, input().split())
    lines.append((a, b))

lines.sort()

b_values = [b for a, b in lines]

lis = []
indexes = []

for i, val in enumerate(b_values):
    pos = bisect.bisect_left(lis, val)
    if pos == len(lis):
        lis.append(val)
    else:
        lis[pos] = val
    indexes.append(pos)

lis_len = len(lis)
print(n - lis_len)

removed = []
target = lis_len - 1

for i in range(n - 1, -1, -1):
    if indexes[i] == target:
        target -= 1
    else:
        removed.append(lines[i][0])

removed.sort()
for x in removed:
    print(x)

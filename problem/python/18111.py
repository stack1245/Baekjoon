import sys
from collections import Counter

input = sys.stdin.readline

n, m, b = map(int, input().split())
flat = []
for _ in range(n):
    flat.extend(map(int, input().split()))

counter = Counter(flat)
min_h = min(counter)
max_h = max(counter)

min_time = float("inf")
result_height = 0

for target in range(max_h, min_h - 1, -1):
    remove = 0
    add = 0

    for height, count in counter.items():
        diff = height - target
        if diff > 0:
            remove += diff * count
        else:
            add -= diff * count

    if remove + b >= add:
        time = remove * 2 + add
        if time < min_time:
            min_time = time
            result_height = target

print(min_time, result_height)

import sys
import heapq

input = sys.stdin.readline

n = int(input())
lines = []

for _ in range(n):
    h, o = map(int, input().split())
    if h > o:
        h, o = o, h
    lines.append((h, o))

d = int(input())

lines.sort(key=lambda x: x[1])

heap = []
max_count = 0

for start, end in lines:
    if end - start <= d:
        heapq.heappush(heap, start)

        while heap and heap[0] < end - d:
            heapq.heappop(heap)

        max_count = max(max_count, len(heap))

print(max_count)

import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

jewels.sort()
bags.sort()

answer = 0
heap = []
j = 0

for bag in bags:
    while j < N and jewels[j][0] <= bag:
        heapq.heappush(heap, -jewels[j][1])
        j += 1

    if heap:
        answer -= heapq.heappop(heap)

print(answer)

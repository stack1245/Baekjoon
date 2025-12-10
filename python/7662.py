import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    min_heap = []
    max_heap = []
    count = defaultdict(int)

    for _ in range(k):
        op, n = input().split()
        n = int(n)

        if op == "I":
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
            count[n] += 1
        else:
            if n == 1:
                while max_heap and count[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    count[-heapq.heappop(max_heap)] -= 1
            else:
                while min_heap and count[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    count[heapq.heappop(min_heap)] -= 1

    while min_heap and count[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and count[-max_heap[0]] == 0:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0], min_heap[0])
    else:
        print("EMPTY")

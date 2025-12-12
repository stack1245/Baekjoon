import heapq
import sys

input = sys.stdin.readline

n = int(input())
arr = tuple(map(int, input().split()))
m = int(input())

ops = []
for _ in range(m):
    l, r, c = map(int, input().split())
    ops.append((l - 1, r - 1, c))

target = tuple(sorted(arr))

if arr == target:
    print(0)
else:
    dist = {arr: 0}
    pq = [(0, arr)]

    found = False
    while pq:
        cost, state = heapq.heappop(pq)

        if state == target:
            print(cost)
            found = True
            break

        if cost > dist.get(state, float("inf")):
            continue

        for l, r, c in ops:
            new_state = list(state)
            new_state[l], new_state[r] = new_state[r], new_state[l]
            new_state = tuple(new_state)

            new_cost = cost + c

            if new_cost < dist.get(new_state, float("inf")):
                dist[new_state] = new_cost
                heapq.heappush(pq, (new_cost, new_state))

    if not found:
        print(-1)

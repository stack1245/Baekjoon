import sys

input = sys.stdin.readline

K, N = map(int, input().split())
cables = []
for _ in range(K):
    cables.append(int(input()))

left, right = 1, max(cables)
result = 0

while left <= right:
    mid = (left + right) // 2

    count = sum(cable // mid for cable in cables)

    if count >= N:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

left, right = 0, max(trees)
result = 0

while left <= right:
    mid = (left + right) // 2

    total = sum(tree - mid if tree > mid else 0 for tree in trees)

    if total >= M:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)

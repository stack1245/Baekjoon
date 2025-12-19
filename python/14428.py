import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

size = 1
while size < n:
    size *= 2
tree = [(float("inf"), 0)] * (size * 2)

for i in range(n):
    tree[size + i] = (arr[i], i + 1)

for i in range(size - 1, 0, -1):
    tree[i] = min(tree[i * 2], tree[i * 2 + 1])


def update(idx, val):
    idx += size
    tree[idx] = (val, idx - size + 1)
    while idx > 1:
        idx //= 2
        tree[idx] = min(tree[idx * 2], tree[idx * 2 + 1])


def query(left, right):
    left += size
    right += size
    result = (float("inf"), 0)
    while left <= right:
        if left % 2 == 1:
            result = min(result, tree[left])
            left += 1
        if right % 2 == 0:
            result = min(result, tree[right])
            right -= 1
        left //= 2
        right //= 2
    return result[1]


m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b - 1, c)
    else:
        print(query(b - 1, c - 1))

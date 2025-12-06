import sys

input = sys.stdin.readline


def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end)
    return tree[node]


def update(node, start, end, idx, diff):
    if idx < start or idx > end:
        return

    tree[node] += diff

    if start != end:
        mid = (start + end) // 2
        update(node * 2, start, mid, idx, diff)
        update(node * 2 + 1, mid + 1, end, idx, diff)


def query(node, start, end, left, right):
    if right < start or left > end:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return query(node * 2, start, mid, left, right) + query(
        node * 2 + 1, mid + 1, end, left, right
    )


n, m, k = map(int, input().split())
arr = [0] + [int(input()) for _ in range(n)]
tree = [0] * (4 * n)

init(1, 1, n)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c - arr[b]
        arr[b] = c
        update(1, 1, n, b, diff)
    else:
        print(query(1, 1, n, b, c))

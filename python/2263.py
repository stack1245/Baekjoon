import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

pos = [0] * (n + 1)
for i in range(n):
    pos[inorder[i]] = i


def solve(in_start, in_end, post_start, post_end):
    if in_start > in_end:
        return

    root = postorder[post_end]
    print(root, end=" ")

    root_idx = pos[root]
    left_size = root_idx - in_start

    solve(in_start, root_idx - 1, post_start, post_start + left_size - 1)
    solve(root_idx + 1, in_end, post_start + left_size, post_end - 1)


solve(0, n - 1, 0, n - 1)

import sys

sys.setrecursionlimit(10**6)

nums = []
for line in sys.stdin:
    nums.append(int(line.strip()))


def postorder(start, end):
    if start > end:
        return

    root = nums[start]
    idx = end + 1

    for i in range(start + 1, end + 1):
        if nums[i] > root:
            idx = i
            break

    postorder(start + 1, idx - 1)
    postorder(idx, end)
    print(root)


postorder(0, len(nums) - 1)

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

result = []


def dfs(start):
    if len(result) == m:
        print(*result)
        return

    prev = 0
    for i in range(start, n):
        if prev != nums[i]:
            result.append(nums[i])
            prev = nums[i]
            dfs(i)
            result.pop()


dfs(0)

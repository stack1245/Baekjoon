def dfs(step):
    if len(s) == m:
        print(" ".join(map(str, s)))
        return
    for i in range(step, n + 1):
        s.append(nums[i - 1])
        dfs(i)
        s.pop()


n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

s = []

dfs(1)

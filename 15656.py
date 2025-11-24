def dfs():
    if len(s) == m:
        print(" ".join(map(str, s)))
        return
    for i in range(1, n + 1):
        s.append(nums[i - 1])
        dfs()
        s.pop()


n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

s = []

dfs()

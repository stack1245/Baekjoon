def dfs(step):
    if len(s) == m:
        print(" ".join(map(str, s)))
        return
    for i in range(step, n + 1):
        s.append(i)
        dfs(i)
        s.pop()


n, m = list(map(int,input().split()))

s = []

dfs(1)

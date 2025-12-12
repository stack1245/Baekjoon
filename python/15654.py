def dfs(step):
    if len(s) == m:
        print(" ".join(map(str, s)))
        return
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            s.append(a[i - 1])
            dfs(i + 1)
            s.pop()
            visited[i] = False


n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()

s = []
visited = [False] * (n + 1)

dfs(1)

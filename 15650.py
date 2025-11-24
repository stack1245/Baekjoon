def dfs(step):
    if len(s) == m:
        print(" ".join(map(str, s)))
        return
    for i in range(step, n + 1):
        if not visited[i]:
            visited[i] = True
            s.append(i)
            dfs(i + 1)
            s.pop()
            visited[i] = False


n, m = map(int, input().split())

s = []
visited = [False] * (n + 1)

dfs(1)

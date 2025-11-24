def dfs(step):
    if step > m:
        print(" ".join(map(str, sequence[1:])))
        return
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            sequence[step] = i
            dfs(step + 1)
            visited[i] = False


n, m = map(int, input().split())

sequence = [0] * (m + 1)
visited = [False] * (n + 1)

dfs(1)

def bf():
    dist = [0] * (n + 1)

    for _ in range(n - 1):
        for s, e, t in edges:
            if dist[s] + t < dist[e]:
                dist[e] = dist[s] + t

    for s, e, t in edges:
        if dist[s] + t < dist[e]:
            return True
    return False


tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    edges = []

    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    print("YES" if bf() else "NO")

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

INF = float("inf")
dp = [[INF] * N for _ in range(1 << N)]
dp[1][0] = 0

for mask in range(1 << N):
    for cur in range(N):
        if dp[mask][cur] == INF:
            continue
        if not (mask & (1 << cur)):
            continue

        for nxt in range(N):
            if mask & (1 << nxt):
                continue
            if W[cur][nxt] == 0:
                continue

            nmask = mask | (1 << nxt)
            dp[nmask][nxt] = min(dp[nmask][nxt], dp[mask][cur] + W[cur][nxt])

ans = INF
for i in range(N):
    if W[i][0] > 0:
        ans = min(ans, dp[(1 << N) - 1][i] + W[i][0])

print(ans)

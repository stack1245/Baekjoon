c, n = map(int, input().split())
cities = [tuple(map(int, input().split())) for _ in range(n)]

dp = [float("inf")] * (c + 101)
dp[0] = 0

for i in range(c + 101):
    if dp[i] == float("inf"):
        continue
    for cost, people in cities:
        if i + people < c + 101:
            dp[i + people] = min(dp[i + people], dp[i] + cost)

print(min(dp[c:]))

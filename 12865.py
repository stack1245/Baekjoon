n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    weight = items[i - 1][0]
    value = items[i - 1][1]
    
    for w in range(k + 1):
        dp[i][w] = dp[i - 1][w]
        
        if w >= weight:
            dp[i][w] = max(dp[i][w], dp[i - 1][w - weight] + value)

print(dp[n][k])

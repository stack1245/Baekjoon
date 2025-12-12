N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

for length in range(1, N):
    for i in range(N - length):
        j = i + length
        dp[i][j] = float("inf")
        for k in range(i, j):
            cost = dp[i][k] + dp[k + 1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1]
            dp[i][j] = min(dp[i][j], cost)

print(dp[0][N - 1])

N = int(input())
MOD = 1000000000

dp = [[[0] * 1024 for _ in range(10)] for _ in range(N + 1)]

for i in range(1, 10):
    dp[1][i][1 << i] = 1

for i in range(1, N):
    for j in range(10):
        for k in range(1024):
            if dp[i][j][k] == 0:
                continue
            
            if j > 0:
                nk = k | (1 << (j - 1))
                dp[i + 1][j - 1][nk] = (dp[i + 1][j - 1][nk] + dp[i][j][k]) % MOD
            
            if j < 9:
                nk = k | (1 << (j + 1))
                dp[i + 1][j + 1][nk] = (dp[i + 1][j + 1][nk] + dp[i][j][k]) % MOD

ans = 0
for i in range(10):
    ans = (ans + dp[N][i][1023]) % MOD

print(ans)

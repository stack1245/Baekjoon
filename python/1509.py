S = input()
n = len(S)

pal = [[False] * n for _ in range(n)]

for i in range(n):
    pal[i][i] = True

for i in range(n - 1):
    if S[i] == S[i + 1]:
        pal[i][i + 1] = True

for length in range(3, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        if S[i] == S[j] and pal[i + 1][j - 1]:
            pal[i][j] = True

dp = [float("inf")] * n

for i in range(n):
    if pal[0][i]:
        dp[i] = 1
    else:
        for j in range(i):
            if pal[j + 1][i]:
                dp[i] = min(dp[i], dp[j] + 1)

print(dp[n - 1])

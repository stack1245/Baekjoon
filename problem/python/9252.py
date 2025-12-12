s1 = input().strip()
s2 = input().strip()

n, m = len(s1), len(s2)
dp = [[""] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
        else:
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

lcs = dp[n][m]
print(len(lcs))
if len(lcs) > 0:
    print(lcs)

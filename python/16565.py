MOD = 10007


def comb(n, r):
    if r > n or r < 0:
        return 0
    if r == 0 or r == n:
        return 1
    return c[n][r]


c = [[0] * 53 for _ in range(53)]
for i in range(53):
    c[i][0] = 1
    for j in range(1, i + 1):
        c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % MOD

n = int(input())

answer = 0
for i in range(1, 14):
    if 4 * i > n:
        break
    if i % 2 == 1:
        answer = (answer + comb(13, i) * comb(52 - 4 * i, n - 4 * i)) % MOD
    else:
        answer = (answer - comb(13, i) * comb(52 - 4 * i, n - 4 * i)) % MOD

print(answer % MOD)

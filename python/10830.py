n, b = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(n)]


def mul(a, b):
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += a[i][k] * b[k][j]
            res[i][j] %= 1000
    return res


def pow(mat, exp):
    if exp == 1:
        return [[mat[i][j] % 1000 for j in range(n)] for i in range(n)]
    if exp % 2 == 0:
        half = pow(mat, exp // 2)
        return mul(half, half)
    return mul(mat, pow(mat, exp - 1))


result = pow(m, b)
for row in result:
    print(*row)

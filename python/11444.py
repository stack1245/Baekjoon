MOD = 1000000007


def mul(a, b):
    return [
        [
            (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % MOD,
            (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % MOD,
        ],
        [
            (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % MOD,
            (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % MOD,
        ],
    ]


def pow(mat, n):
    if n == 1:
        return mat
    if n % 2 == 0:
        half = pow(mat, n // 2)
        return mul(half, half)
    return mul(mat, pow(mat, n - 1))


n = int(input())
if n == 0:
    print(0)
else:
    mat = [[1, 1], [1, 0]]
    result = pow(mat, n)
    print(result[0][1])

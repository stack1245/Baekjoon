MOD = 1000000007


def mul(a, b):
    result = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            for k in range(8):
                result[i][j] = (result[i][j] + a[i][k] * b[k][j]) % MOD
    return result


def pow(mat, n):
    if n == 1:
        return mat
    if n % 2 == 0:
        half = pow(mat, n // 2)
        return mul(half, half)
    return mul(mat, pow(mat, n - 1))


graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0],
]

d = int(input())
result = pow(graph, d)
print(result[0][0])

MOD = 1000000007


def pow(a, b):
    res = 1
    while b:
        if b % 2:
            res = res * a % MOD
        a = a * a % MOD
        b //= 2
    return res


m = int(input())
ans = 0
for _ in range(m):
    n, s = map(int, input().split())
    ans = (ans + s * pow(n, MOD - 2)) % MOD
print(ans)

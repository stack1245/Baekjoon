N, r, c = map(int, input().split())


def solve(n, r, c):
    if n == 0:
        return 0

    half = 2 ** (n - 1)

    if r < half and c < half:
        return solve(n - 1, r, c)
    elif r < half and c >= half:
        return half * half + solve(n - 1, r, c - half)
    elif r >= half and c < half:
        return 2 * half * half + solve(n - 1, r - half, c)
    else:
        return 3 * half * half + solve(n - 1, r - half, c - half)


print(solve(N, r, c))

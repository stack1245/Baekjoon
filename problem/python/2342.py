import sys

input = sys.stdin.readline


def cost(a, b):
    if a == b:
        return 1
    if a == 0:
        return 2
    if abs(a - b) == 2:
        return 4
    return 3


moves = list(map(int, input().split()))[:-1]
dp = {}
dp[(0, 0)] = 0

for move in moves:
    new_dp = {}
    for (l, r), c in dp.items():
        nl, nr = move, r
        key = (nl, nr)
        val = c + cost(l, move)
        if key not in new_dp or new_dp[key] > val:
            new_dp[key] = val

        nl, nr = l, move
        key = (nl, nr)
        val = c + cost(r, move)
        if key not in new_dp or new_dp[key] > val:
            new_dp[key] = val

    dp = new_dp

print(min(dp.values()))

from collections import deque

n = int(input())
a, b, c = map(int, input().split())
nums = list(map(int, input().split()))

s = [0]
for x in nums:
    s.append(s[-1] + x)

dp = [0] * (n + 1)


def y(i):
    return dp[i] + a * s[i] * s[i] - b * s[i]


def x(i):
    return 2 * a * s[i]


def slope(i, j):
    return (y(j) - y(i)) / (x(j) - x(i))


dq = deque([0])

for i in range(1, n + 1):
    while len(dq) >= 2 and slope(dq[0], dq[1]) < s[i]:
        dq.popleft()

    j = dq[0]
    dp[i] = dp[j] + a * (s[i] - s[j]) * (s[i] - s[j]) + b * (s[i] - s[j]) + c

    while len(dq) >= 2 and slope(dq[-2], dq[-1]) > slope(dq[-1], i):
        dq.pop()

    dq.append(i)

print(dp[n])

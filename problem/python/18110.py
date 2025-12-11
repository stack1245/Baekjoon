import sys
import math


def round_custom(x):
    return int(x + 0.5)


n = int(sys.stdin.readline())

if n == 0:
    print(0)
else:
    opinions = []
    for _ in range(n):
        opinions.append(int(sys.stdin.readline()))

    opinions.sort()

    exclude_count = int(n * 0.15 + 0.5)

    if exclude_count > 0:
        trimmed = opinions[exclude_count : n - exclude_count]
    else:
        trimmed = opinions

    avg = sum(trimmed) / len(trimmed)
    result = round_custom(avg)

    print(result)

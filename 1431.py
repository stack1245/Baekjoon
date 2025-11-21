n = int(input())

serials = []
for _ in range(n):
    serials.append(input())


def digit_sum(s):
    return sum(int(c) for c in s if c.isdigit())


serials.sort(key=lambda x: (len(x), digit_sum(x), x))

print(*serials, sep="\n")

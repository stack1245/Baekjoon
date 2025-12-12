def count_ones(x):
    if x <= 0:
        return 0

    cnt = 0
    bit = 0
    num = x

    while (1 << bit) <= x:
        cycle = 1 << (bit + 1)
        complete = (x + 1) // cycle
        cnt += complete * (1 << bit)
        remain = (x + 1) % cycle
        cnt += max(0, remain - (1 << bit))
        bit += 1

    return cnt


A, B = map(int, input().split())
print(count_ones(B) - count_ones(A - 1))

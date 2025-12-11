n = int(input())

count = 0
col_used = [False] * n
diag1_used = [False] * (2 * n - 1)
diag2_used = [False] * (2 * n - 1)


def solve(row):
    global count
    if row == n:
        count += 1
        return

    for col in range(n):
        d1 = row + col
        d2 = row - col + n - 1

        if not col_used[col] and not diag1_used[d1] and not diag2_used[d2]:
            col_used[col] = diag1_used[d1] = diag2_used[d2] = True
            solve(row + 1)
            col_used[col] = diag1_used[d1] = diag2_used[d2] = False


solve(0)
print(count)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

black = []
white = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            if (i + j) % 2 == 0:
                black.append((i, j))
            else:
                white.append((i, j))


def solve(positions):
    used1 = set()
    used2 = set()
    max_count = 0

    def backtrack(idx, count):
        nonlocal max_count

        if idx == len(positions):
            max_count = max(max_count, count)
            return

        if count + len(positions) - idx <= max_count:
            return

        x, y = positions[idx]
        diag1 = x + y
        diag2 = x - y

        if diag1 not in used1 and diag2 not in used2:
            used1.add(diag1)
            used2.add(diag2)
            backtrack(idx + 1, count + 1)
            used1.remove(diag1)
            used2.remove(diag2)

        backtrack(idx + 1, count)

    backtrack(0, 0)
    return max_count


print(solve(black) + solve(white))

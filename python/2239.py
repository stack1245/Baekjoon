board = [list(map(int, list(input()))) for _ in range(9)]
row_used = [[False] * 10 for _ in range(9)]
col_used = [[False] * 10 for _ in range(9)]
box_used = [[False] * 10 for _ in range(9)]

zeros = []
for i in range(9):
    for j in range(9):
        num = board[i][j]
        if num == 0:
            zeros.append((i, j))
        else:
            row_used[i][num] = True
            col_used[j][num] = True
            box_used[(i // 3) * 3 + j // 3][num] = True


def solve(idx):
    if idx == len(zeros):
        return True

    x, y = zeros[idx]
    box_idx = (x // 3) * 3 + y // 3

    for num in range(1, 10):
        if not row_used[x][num] and not col_used[y][num] and not box_used[box_idx][num]:
            board[x][y] = num
            row_used[x][num] = True
            col_used[y][num] = True
            box_used[box_idx][num] = True

            if solve(idx + 1):
                return True

            board[x][y] = 0
            row_used[x][num] = False
            col_used[y][num] = False
            box_used[box_idx][num] = False

    return False


solve(0)

for row in board:
    print("".join(map(str, row)))

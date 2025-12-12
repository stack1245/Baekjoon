n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def move(b, d):
    new = [[0] * n for _ in range(n)]

    if d == 0:
        for j in range(n):
            idx = 0
            merged = False
            for i in range(n):
                if b[i][j] != 0:
                    if idx > 0 and new[idx - 1][j] == b[i][j] and not merged:
                        new[idx - 1][j] *= 2
                        merged = True
                    else:
                        new[idx][j] = b[i][j]
                        idx += 1
                        merged = False

    elif d == 1:
        for j in range(n):
            idx = n - 1
            merged = False
            for i in range(n - 1, -1, -1):
                if b[i][j] != 0:
                    if idx < n - 1 and new[idx + 1][j] == b[i][j] and not merged:
                        new[idx + 1][j] *= 2
                        merged = True
                    else:
                        new[idx][j] = b[i][j]
                        idx -= 1
                        merged = False

    elif d == 2:
        for i in range(n):
            idx = 0
            merged = False
            for j in range(n):
                if b[i][j] != 0:
                    if idx > 0 and new[i][idx - 1] == b[i][j] and not merged:
                        new[i][idx - 1] *= 2
                        merged = True
                    else:
                        new[i][idx] = b[i][j]
                        idx += 1
                        merged = False

    else:
        for i in range(n):
            idx = n - 1
            merged = False
            for j in range(n - 1, -1, -1):
                if b[i][j] != 0:
                    if idx < n - 1 and new[i][idx + 1] == b[i][j] and not merged:
                        new[i][idx + 1] *= 2
                        merged = True
                    else:
                        new[i][idx] = b[i][j]
                        idx -= 1
                        merged = False

    return new


def dfs(b, cnt):
    if cnt == 5:
        return max(max(row) for row in b)

    result = 0
    for d in range(4):
        result = max(result, dfs(move(b, d), cnt + 1))

    return result


print(dfs(board, 0))

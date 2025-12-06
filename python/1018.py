n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input())

pattern1 = []
pattern2 = []

for i in range(8):
    row1 = ""
    row2 = ""
    for j in range(8):
        if (i + j) % 2 == 0:
            row1 += "W"
            row2 += "B"
        else:
            row1 += "B"
            row2 += "W"
    pattern1.append(row1)
    pattern2.append(row2)

min_count = 64

for start_i in range(n - 7):
    for start_j in range(m - 7):
        count1 = 0
        count2 = 0

        for i in range(8):
            for j in range(8):
                current = board[start_i + i][start_j + j]

                if current != pattern1[i][j]:
                    count1 += 1

                if current != pattern2[i][j]:
                    count2 += 1

        min_count = min(min_count, count1, count2)

print(min_count)

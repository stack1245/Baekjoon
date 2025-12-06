import sys

input = sys.stdin.readline

N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

white = 0
blue = 0


def check_color(x, y, size):
    color = paper[y][x]
    for i in range(y, y + size):
        for j in range(x, x + size):
            if paper[i][j] != color:
                return -1
    return color


def divide(x, y, size):
    global white, blue

    color = check_color(x, y, size)

    if color == 0:
        white += 1
    elif color == 1:
        blue += 1
    else:
        half = size // 2
        divide(x, y, half)
        divide(x + half, y, half)
        divide(x, y + half, half)
        divide(x + half, y + half, half)


divide(0, 0, N)

print(white)
print(blue)

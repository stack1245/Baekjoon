n = int(input())
stars = [[" "] * (2 * n - 1) for _ in range(n)]


def draw(x, y, size):
    if size == 3:
        stars[x][y] = "*"
        stars[x + 1][y - 1] = stars[x + 1][y + 1] = "*"
        for i in range(y - 2, y + 3):
            stars[x + 2][i] = "*"
        return

    half = size // 2
    draw(x, y, half)
    draw(x + half, y - half, half)
    draw(x + half, y + half, half)


draw(0, n - 1, n)

for line in stars:
    print("".join(line).rstrip())

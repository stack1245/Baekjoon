import sys

input = sys.stdin.readline

r, c, m = map(int, input().split())
sharks = {}

for _ in range(m):
    row, col, s, d, z = map(int, input().split())
    sharks[(row - 1, col - 1)] = [s, d - 1, z]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

result = 0

for person in range(c):
    for row in range(r):
        if (row, person) in sharks:
            result += sharks[(row, person)][2]
            del sharks[(row, person)]
            break

    new_sharks = {}
    for (x, y), (s, d, z) in sharks.items():
        if d < 2:
            move = s % (2 * (r - 1))
        else:
            move = s % (2 * (c - 1))

        nx, ny, nd = x, y, d
        for _ in range(move):
            nx += dx[nd]
            ny += dy[nd]

            if nx < 0 or nx >= r:
                nd = 1 - nd
                nx += 2 * dx[nd]
            if ny < 0 or ny >= c:
                nd = 5 - nd
                ny += 2 * dy[nd]

        if (nx, ny) not in new_sharks or new_sharks[(nx, ny)][2] < z:
            new_sharks[(nx, ny)] = [s, nd, z]

    sharks = new_sharks

print(result)

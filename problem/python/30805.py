n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

result = []
i, j = 0, 0

while i < n and j < m:
    max_val = -1
    max_i, max_j = -1, -1

    for ii in range(i, n):
        for jj in range(j, m):
            if a[ii] == b[jj] and a[ii] > max_val:
                max_val = a[ii]
                max_i, max_j = ii, jj

    if max_val == -1:
        break

    result.append(max_val)
    i, j = max_i + 1, max_j + 1

print(len(result))
if result:
    print(*result)

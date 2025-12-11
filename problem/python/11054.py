n = int(input())
a = list(map(int, input().split()))

inc = [1] * n
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            inc[i] = max(inc[i], inc[j] + 1)

dec = [1] * n
for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if a[j] < a[i]:
            dec[i] = max(dec[i], dec[j] + 1)

print(max(inc[i] + dec[i] - 1 for i in range(n)))

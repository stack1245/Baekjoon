n = int(input())
a = list(map(int, input().split()))

left, right = 0, n - 1
best = abs(a[left] + a[right])
result = (a[left], a[right])

while left < right:
    s = a[left] + a[right]
    if abs(s) < best:
        best = abs(s)
        result = (a[left], a[right])

    if s < 0:
        left += 1
    elif s > 0:
        right -= 1
    else:
        break

print(result[0], result[1])

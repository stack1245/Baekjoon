n, s = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 0
total = 0
min_len = n + 1

while True:
    if total >= s:
        min_len = min(min_len, right - left)
        total -= arr[left]
        left += 1
    elif right == n:
        break
    else:
        total += arr[right]
        right += 1

if min_len == n + 1:
    print(0)
else:
    print(min_len)

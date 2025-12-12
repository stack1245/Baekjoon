N = int(input())
arr = list(map(int, input().split()))
arr.sort()

min_val = float("inf")
answer = []

for i in range(N - 2):
    left = i + 1
    right = N - 1

    while left < right:
        s = arr[i] + arr[left] + arr[right]

        if abs(s) < min_val:
            min_val = abs(s)
            answer = [arr[i], arr[left], arr[right]]

        if s < 0:
            left += 1
        elif s > 0:
            right -= 1
        else:
            break

print(*answer)

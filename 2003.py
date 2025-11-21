N, M = map(int, input().split())
A = list(map(int, input().split()))

count = 0
left = 0
current_sum = 0

for right in range(N):
    current_sum += A[right]

    while current_sum > M:
        current_sum -= A[left]
        left += 1

    if current_sum == M:
        count += 1

print(count)

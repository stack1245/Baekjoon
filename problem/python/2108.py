import sys
from collections import Counter

n = int(sys.stdin.readline())
numbers = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

mean = sum(numbers) / n
mean = int(mean + 0.5) if mean >= 0 else int(mean - 0.5)
print(mean)

median = numbers[n // 2]
print(median)

counter = Counter(numbers)
max_freq = max(counter.values())
modes = [num for num, freq in counter.items() if freq == max_freq]
modes.sort()

if len(modes) > 1:
    print(modes[1])
else:
    print(modes[0])

range_val = numbers[-1] - numbers[0]
print(range_val)

a, b = map(int, input().split())

sequence = []
for i in range(1, b + 1):
    for j in range(1, i + 1):
        sequence.append(i)

print(sum(sequence[a - 1 : b]))

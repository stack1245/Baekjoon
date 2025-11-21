n = int(input())

for fives in range(n // 5, -1, -1):
    remainder = n - fives * 5
    if remainder % 2 == 0:
        print(fives + remainder // 2)
        break
else:
    print(-1)

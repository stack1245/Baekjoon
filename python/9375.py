import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    clothes = {}

    for _ in range(n):
        name, category = input().split()
        if category in clothes:
            clothes[category] += 1
        else:
            clothes[category] = 1

    result = 1
    for count in clothes.values():
        result *= count + 1

    print(result - 1)

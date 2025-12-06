import sys

input = sys.stdin.readline

N = int(input())
coords = list(map(int, input().split()))

sorted_unique = sorted(set(coords))

compress_dict = {val: idx for idx, val in enumerate(sorted_unique)}

result = [compress_dict[coord] for coord in coords]
print(" ".join(map(str, result)))

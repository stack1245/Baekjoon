from itertools import combinations

L, C = map(int, input().split())
arr = list(input().split())
arr.sort()

for comb in combinations(arr, L):
    vowel_count = 0
    for char in comb:
        if char in "aeiou":
            vowel_count += 1

    consonant_count = L - vowel_count

    if vowel_count >= 1 and consonant_count >= 2:
        print("".join(comb))

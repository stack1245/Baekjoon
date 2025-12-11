n = int(input())
m = int(input())
s = input()

count = 0
i = 0
pattern_count = 0

while i < m - 1:
    if s[i : i + 3] == "IOI":
        pattern_count += 1
        i += 2
        if pattern_count == n:
            count += 1
            pattern_count -= 1
    else:
        i += 1
        pattern_count = 0

print(count)

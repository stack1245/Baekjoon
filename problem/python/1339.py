n = int(input())
words = [input().strip() for _ in range(n)]

weights = {}
for word in words:
    for i, char in enumerate(reversed(word)):
        weights[char] = weights.get(char, 0) + 10**i

sorted_chars = sorted(weights.keys(), key=lambda x: weights[x], reverse=True)

result = 0
for word in words:
    value = 0
    for char in word:
        digit = 9 - sorted_chars.index(char)
        value = value * 10 + digit
    result += value

print(result)

words = [input() for _ in range(5)]
result = []

for i in range(15):
    for word in words:
        if i < len(word):
            result.append(word[i])

print("".join(result))

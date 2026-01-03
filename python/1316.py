n = int(input())

count = 0
for _ in range(n):
    word = input()
    is_group = True
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            if word[i] in word[i + 1 :]:
                is_group = False
                break
    if is_group:
        count += 1

print(count)

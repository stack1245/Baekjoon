word = input().upper()
unique = list(set(word))

count = []
for x in unique:
    count.append(word.count(x))

if count.count(max(count)) > 1:
    print("?")
else:
    print(unique[count.index(max(count))])

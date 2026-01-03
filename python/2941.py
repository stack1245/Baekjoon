word = input()
croatian = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for c in croatian:
    word = word.replace(c, "*")

print(len(word))

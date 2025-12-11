n = int(input())

i = 1
while i * i <= n:
    if i * i == n:
        print(1)
        exit()
    i += 1

i = 1
while i * i <= n:
    j = int((n - i * i) ** 0.5)
    if i * i + j * j == n:
        print(2)
        exit()
    i += 1

temp = n
while temp % 4 == 0:
    temp //= 4

if temp % 8 == 7:
    print(4)
else:
    print(3)

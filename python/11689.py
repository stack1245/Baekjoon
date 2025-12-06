n = int(input())

result = n
temp = n

i = 2
while i * i <= temp:
    if temp % i == 0:
        result = result - result // i
        while temp % i == 0:
            temp //= i
    i += 1

if temp > 1:
    result = result - result // temp

print(result)

isbn = input()

weights = [1, 3] * 7

star_index = isbn.index('*')

for digit in range(10):
    total = 0
    for i in range(13):
        if i == star_index:
            total += digit * weights[i]
        else:
            total += int(isbn[i]) * weights[i]
    
    if total % 10 == 0:
        print(digit)
        break

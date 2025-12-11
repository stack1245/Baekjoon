inputs = [input() for _ in range(3)]

next_num = 0
for i in range(3):
    if inputs[i].isdigit():
        next_num = int(inputs[i]) + (3 - i)
        break

if next_num % 15 == 0:
    print("FizzBuzz")
elif next_num % 3 == 0:
    print("Fizz")
elif next_num % 5 == 0:
    print("Buzz")
else:
    print(next_num)

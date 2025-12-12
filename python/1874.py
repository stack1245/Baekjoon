n = int(input())
target = []
for _ in range(n):
    target.append(int(input()))

stack = []
result = []
current = 1
possible = True

for num in target:
    while current <= num:
        stack.append(current)
        result.append("+")
        current += 1

    if stack and stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        possible = False
        break

if possible:
    for op in result:
        print(op)
else:
    print("NO")

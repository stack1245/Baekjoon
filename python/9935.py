s = input()
bomb = input()

stack = []
bomb_len = len(bomb)

for char in s:
    stack.append(char)

    if len(stack) >= bomb_len and "".join(stack[-bomb_len:]) == bomb:
        for _ in range(bomb_len):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")

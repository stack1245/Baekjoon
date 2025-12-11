s = input()
stack = []
result = []

for c in s:
    if c.isalpha():
        result.append(c)
    elif c == "(":
        stack.append(c)
    elif c == ")":
        while stack and stack[-1] != "(":
            result.append(stack.pop())
        stack.pop()
    else:
        if c in "*/":
            while stack and stack[-1] in "*/":
                result.append(stack.pop())
        else:
            while stack and stack[-1] != "(":
                result.append(stack.pop())
        stack.append(c)

while stack:
    result.append(stack.pop())

print("".join(result))

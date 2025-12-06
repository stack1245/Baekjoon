import sys

m = int(sys.stdin.readline())
s = 0

for _ in range(m):
    command = sys.stdin.readline().strip().split()

    if command[0] == "add":
        x = int(command[1])
        s |= 1 << x
    elif command[0] == "remove":
        x = int(command[1])
        s &= ~(1 << x)
    elif command[0] == "check":
        x = int(command[1])
        if s & (1 << x):
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        x = int(command[1])
        s ^= 1 << x
    elif command[0] == "all":
        s = (1 << 21) - 1
    elif command[0] == "empty":
        s = 0

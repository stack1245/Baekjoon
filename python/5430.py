import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().strip()
    n = int(input())
    arr_str = input().strip()

    if n == 0:
        dq = deque()
    else:
        arr = list(map(int, arr_str[1:-1].split(",")))
        dq = deque(arr)

    is_reversed = False
    error = False

    for cmd in p:
        if cmd == "R":
            is_reversed = not is_reversed
        elif cmd == "D":
            if not dq:
                error = True
                break
            if is_reversed:
                dq.pop()
            else:
                dq.popleft()

    if error:
        print("error")
    else:
        if is_reversed:
            dq.reverse()
        print("[" + ",".join(map(str, dq)) + "]")

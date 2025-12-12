import bisect

n = int(input())
a = list(map(int, input().split()))

lis = []
trace = []

for num in a:
    pos = bisect.bisect_left(lis, num)
    if pos == len(lis):
        lis.append(num)
    else:
        lis[pos] = num
    trace.append((pos, num))

length = len(lis)
result = []
idx = length - 1

for i in range(n - 1, -1, -1):
    if trace[i][0] == idx:
        result.append(trace[i][1])
        idx -= 1
        if idx < 0:
            break

result.reverse()
print(length)
print(*result)

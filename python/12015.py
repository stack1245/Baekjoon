import bisect

N = int(input())
A = list(map(int, input().split()))

lis = []
for num in A:
    pos = bisect.bisect_left(lis, num)
    if pos == len(lis):
        lis.append(num)
    else:
        lis[pos] = num

print(len(lis))

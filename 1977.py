import math

n = int(input())
m = int(input())

pows = []
for i in range(n, m + 1):
    if math.sqrt(i) == int(math.sqrt(i)):
        pows.append(i)

if not pows:
    print(-1)
else:
    print(sum(pows))
    print(min(pows))

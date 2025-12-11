N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

tshirt_bundles = 0
for size in sizes:
    if size > 0:
        tshirt_bundles += (size + T - 1) // T

pen_bundles = N // P
pen_individual = N % P

print(tshirt_bundles)
print(pen_bundles, pen_individual)

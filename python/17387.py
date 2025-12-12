def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

c1 = ccw(x1, y1, x2, y2, x3, y3)
c2 = ccw(x1, y1, x2, y2, x4, y4)
c3 = ccw(x3, y3, x4, y4, x1, y1)
c4 = ccw(x3, y3, x4, y4, x2, y2)

if c1 * c2 == 0 and c3 * c4 == 0:
    if (
        min(x1, x2) <= max(x3, x4)
        and min(x3, x4) <= max(x1, x2)
        and min(y1, y2) <= max(y3, y4)
        and min(y3, y4) <= max(y1, y2)
    ):
        print(1)
    else:
        print(0)
elif c1 * c2 <= 0 and c3 * c4 <= 0:
    print(1)
else:
    print(0)

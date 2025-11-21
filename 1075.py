N = int(input())
F = int(input())

_10 = 0
_100 = 0

while str(_100) + str(_10) != "100":
    if int(str(N)[:-2] + str(_100) + str(_10)) % F == 0:
        break
    else:
        _10 += 1
        if _10 == 10:
            _10 = 0
            _100 += 1

print(str(_100) + str(_10))

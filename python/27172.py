n = int(input())
x = list(map(int, input().split()))

max_val = max(x)
exist = [False] * (max_val + 1)
score = [0] * (max_val + 1)

for num in x:
    exist[num] = True

for num in x:
    for multiple in range(num * 2, max_val + 1, num):
        if exist[multiple]:
            score[num] += 1
            score[multiple] -= 1

print(" ".join(str(score[num]) for num in x))

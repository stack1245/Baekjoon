points = []
x_dict = {}
y_dict = {}

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
    
    if x not in x_dict:
        x_dict[x] = 0
    x_dict[x] += 1
    
    if y not in y_dict:
        y_dict[y] = 0
    y_dict[y] += 1

result = 0

for x, y in points:
    same_x = x_dict[x] - 1
    same_y = y_dict[y] - 1
    
    result += same_x * same_y

print(result)

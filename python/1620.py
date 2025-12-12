import sys

n, m = map(int, sys.stdin.readline().split())

pokemon_by_num = {}
pokemon_by_name = {}

for i in range(1, n + 1):
    name = sys.stdin.readline().strip()
    pokemon_by_num[i] = name
    pokemon_by_name[name] = i

for _ in range(m):
    query = sys.stdin.readline().strip()
    
    if query.isdigit():
        print(pokemon_by_num[int(query)])
    else:
        print(pokemon_by_name[query])

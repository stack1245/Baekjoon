from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))
    
    queue = deque()
    for i in range(n):
        queue.append((priorities[i], i))
    
    print_count = 0
    
    while queue:
        current = queue.popleft()
        
        if any(current[0] < doc[0] for doc in queue):
            queue.append(current)
        else:
            print_count += 1
            if current[1] == m:
                print(print_count)
                break

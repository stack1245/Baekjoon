from collections import deque

n, m = map(int, input().split())
board = [0] * 101

for _ in range(n + m):
    x, y = map(int, input().split())
    board[x] = y

queue = deque([(1, 0)])
visited = [False] * 101
visited[1] = True

while queue:
    pos, count = queue.popleft()
    
    if pos == 100:
        print(count)
        break
    
    for dice in range(1, 7):
        next_pos = pos + dice
        
        if next_pos <= 100 and not visited[next_pos]:
            if board[next_pos]:
                next_pos = board[next_pos]
            
            if not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, count + 1))

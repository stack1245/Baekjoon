n = int(input())
a = list(map(int, input().split()))
op = list(map(int, input().split()))

mx = -1e9
mn = 1e9

def dfs(idx, res, p, m, mul, d):
    global mx, mn
    
    if idx == n:
        mx = max(mx, res)
        mn = min(mn, res)
        return
    
    if p > 0:
        dfs(idx + 1, res + a[idx], p - 1, m, mul, d)
    if m > 0:
        dfs(idx + 1, res - a[idx], p, m - 1, mul, d)
    if mul > 0:
        dfs(idx + 1, res * a[idx], p, m, mul - 1, d)
    if d > 0:
        dfs(idx + 1, int(res / a[idx]), p, m, mul, d - 1)

dfs(1, a[0], op[0], op[1], op[2], op[3])

print(int(mx))
print(int(mn))

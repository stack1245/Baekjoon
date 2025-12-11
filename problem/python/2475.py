nums = list(map(int, input().split()))
result = sum(n**2 for n in nums) % 10
print(result)

receipt_total = int(input())
item_count = int(input())

calculated_total = 0
for _ in range(item_count):
    item_price, item_quantity = map(int, input().split())
    calculated_total += item_price * item_quantity

if receipt_total == calculated_total:
    print("Yes")
else:
    print("No")

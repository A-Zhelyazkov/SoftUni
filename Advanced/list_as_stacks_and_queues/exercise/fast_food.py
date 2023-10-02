from collections import deque
food = int(input())
food_orders = deque(int(i) for i in input().split())

print(max(food_orders))

while food_orders:
    current_order = food_orders.popleft()

    if food >= current_order:
        food -= current_order
    else:
        food_orders.insert(0, current_order)
        break

if food_orders:
    print(f"Orders left: {' '.join(str(i) for i in food_orders)}")
else:
    print("Orders complete")

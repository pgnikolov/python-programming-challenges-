# from collections import deque
#
# food = int(input())
#
# orders = deque([int(i) for i in input().split()])
#
# print(max(orders))
#
# while True:
#     if len(orders) == 0:
#         break
#     if food < orders[0]:
#         break
#     else:
#         food -= orders[0]
#         orders.popleft()
#
# if len(orders) == 0:
#     print('Orders complete')
# else:
#     orders = list(str(n) for n in orders)
#     print(f'Orders left: {" ".join(orders)}')

from collections import deque
food_qnt = int(input())

orders_food = deque(int(num) for num in input().split())
print(max(orders_food))

while True:
	if orders_food and orders_food[0] <= food_qnt:
		food_qnt -= orders_food.popleft()
	else:
		break

if orders_food:
	print(f"Orders left: {' '.join(map(str, orders_food))}")
else:
	print("Orders complete")

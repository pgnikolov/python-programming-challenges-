from collections import deque

food = int(input())

orders = deque([int(i) for i in input().split()])

print(max(orders))

while True:
    if len(orders) == 0:
        break
    if food < orders[0]:
        break
    else:
        food -= orders[0]
        orders.popleft()

if len(orders) == 0:
    print('Orders complete')
else:
    orders = list(str(n) for n in orders)
    print(f'Orders left: {" ".join(orders)}')

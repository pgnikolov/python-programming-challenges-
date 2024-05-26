from collections import deque

food = int(input())
orders = deque([int(x) for x in input().split(' ')])

print(max(orders))

while len(orders) > 0:
    if food < orders[0]:
        print(f"Orders left: ", end='')
        print(*orders, sep=' ')
        break

    served = orders.popleft()
    food -= served
else:
    print("Orders complete")

from collections import deque

choco = deque([int(num) for num in input().split(", ")])
milk_cups = deque([int(num) for num in input().split(", ")])

shakes_to_do = 0

while True:
    if len(choco) == 0 or len(milk_cups) == 0 or shakes_to_do == 5:
        break
    if choco[-1] <= 0:
        choco.pop()
    if milk_cups[0] <= 0:
        milk_cups.popleft()
    if choco and milk_cups:
        if choco[-1] == milk_cups[0]:
            shakes_to_do += 1
            choco.pop()
            milk_cups.popleft()
        else:
            milk_cups.rotate(-1)
            choco[-1] -= 5
    else:
        continue

if shakes_to_do == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if len(choco) > 0:
    print(f"Chocolate: {', '.join(map(str, choco))} ")
else:
    print("Chocolate: empty")

if len(milk_cups) > 0:
    print(f"Milk: {', '.join(map(str, milk_cups))} ")
else:
    print("Milk: empty")

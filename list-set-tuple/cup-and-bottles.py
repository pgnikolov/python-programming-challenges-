from collections import deque

cups = deque(map(int, input().split()))
bottles = deque(map(int, input().split()))
wasted_water = 0

while cups and bottles:
    current_bottle = bottles.pop()
    current_cup = cups.popleft()

    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup
    else:
        cups.appendleft(current_cup - current_bottle)

if cups:
    print(f"Cups: {' '.join(map(str, cups))}")
if bottles:
    print(f"Bottles: {' '.join(map(str, bottles))}")

print(f"Wasted litters of water: {wasted_water}")

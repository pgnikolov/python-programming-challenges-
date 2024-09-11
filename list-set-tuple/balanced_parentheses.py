from collections import deque

pairs = ['()', '{}', '[]']
parentheses = deque(i for i in input())
counter = len(parentheses) / 2

while counter > 0:
    firt = parentheses[0]
    last = parentheses[-1]
    counter -= 1
    if firt + last in pairs:
        parentheses.pop()
        parentheses.popleft()

if len(parentheses) == 0:
    print("YES")
else:
    print("NO")


from collections import deque

numstack = deque()
commands_qt = int(input())

COMMAND_PUSH = '1'
COMMAND_DELETE = '2'
COMMAND_MAXIMUM = '3'
COMMAND_MINIMUM = '4'

for command_number in range(commands_qt):

    command = input()

    if command.startswith(COMMAND_PUSH):
        number = command.split()
        numstack.append(int(number[1]))

    if len(numstack) > 0:
        if command.startswith(COMMAND_DELETE):
            numstack.pop()

        elif command.startswith(COMMAND_MAXIMUM):
            print(max(numstack))

        elif command.startswith(COMMAND_MINIMUM):
            print(min(numstack))

numstack.reverse()
print(*numstack, sep=", ")

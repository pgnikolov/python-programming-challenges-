# Write a program that:
#     • Reads an input string
#     • Reverses it using a stack
#     • Prints the result back on the console

stak = [letter for letter in input()]

result = []

for i in range(len(stak)):
    result.append(stak.pop())

print("".join(result))

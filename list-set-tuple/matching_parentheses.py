# You are given an algebraic expression with parentheses. Scan through the string and extract each set of parentheses.
# Print the result back on the console.

expression = input()

stack = []

for i in range(len(expression)):
    if expression[i] == "(":
        stack.append(i)
    elif expression[i] == ")":
        start = stack.pop()
        print(expression[start:i + 1])


# expr_str = [char for char in input()]
#
# result = []
# start_index = []
#
# for i in range(len(expr_str)):
# 	if expr_str[i] == "(":
# 		start_index.append(i)
# 	elif expr_str[i] == ")":
# 		result.append("".join(expr_str[start_index.pop(): i + 1]))
#
# print("\n".join(result))

expression = input()

stack = []

for i in range(len(expression)):
    if expression[i] == "(":
        stack.append(i)
    elif expression[i] == ")":
        start = stack.pop()
        print(expression[start:i + 1])


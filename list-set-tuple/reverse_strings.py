# stak = [letter for letter in input()]
#
# result = []
#
# for i in range(len(stak)):
#     result.append(stak.pop())
#
# print("".join(result))


string_ = [char for char in (input())]

rev_string = [string_.pop() for i in range(len(string_))]
print("".join(rev_string))

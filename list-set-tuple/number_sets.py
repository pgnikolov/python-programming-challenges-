# first_set = set([int(el) for el in input().split()])
# second_set = set([int(el) for el in input().split()])
#
# # print(first_set)
# # print(second_set)
#
# number_of_commands = int(input())
#
# for _ in range(number_of_commands):
#     current_command_tokens = input().split()
#     real_command = ' '.join(current_command_tokens[:2])
#     # print(real_command)
#     current_set = set([int(el) for el in current_command_tokens[2:]])
#     # print(current_set)
#
#     if real_command == 'Add First':  # TODO do this with mapper { command: function }
#         first_set = first_set.union(current_set)
#     elif real_command == 'Add Second':
#         second_set = second_set.union(current_set)
#     elif real_command == 'Remove First':
#         first_set = first_set.difference(current_set)
#     elif real_command == 'Remove Second':
#         second_set = second_set.difference(current_set)
#     elif real_command == 'Check Subset':
#         is_subset = first_set.issubset(second_set) or second_set.issubset(first_set)
#         print(is_subset)
#
# first_set_as_sorted_list = sorted(list(first_set))
# second_set_as_sorted_list = sorted(list(second_set))
# # print(', '.join([str(el) for el in first_set_as_sorted_list]))
# # print(', '.join([str(el) for el in second_set_as_sorted_list]))
#
# print(*first_set_as_sorted_list, sep=", ")
# print(*second_set_as_sorted_list, sep=", ")

first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

functions = {
    'Add First': lambda numbers: [first_set.add(x) for x in numbers],
    'Add Second': lambda numbers: [second_set.add(x) for x in numbers],
    'Remove First': lambda numbers: [first_set.discard(x) for x in numbers],
    'Remove Second': lambda numbers: [second_set.discard(x) for x in numbers],
    'Check Subset': lambda numbers:
    print('True') if first_set.issubset(second_set) or second_set.issubset(first_set) else print('False')
}

for _ in range(int(input())):
    command = input().split()
    func = command[0] + ' ' + command[1]
    number_list = [int(x) for x in command[2:]]

    functions[func](number_list)

print(*(sorted(first_set)), sep=', ')
print(*(sorted(second_set)), sep=', ')

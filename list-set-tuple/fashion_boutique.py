# clothes = [int(x) for x in input().split()]
# rack_capacity = int(input())
# new_rack_capacity = rack_capacity
# racks_used = 1
#
# for _ in range(len(clothes)):
#     clothe = clothes.pop()
#     if new_rack_capacity - clothe < 0:
#         racks_used += 1
#         new_rack_capacity = rack_capacity
#     new_rack_capacity -= clothe
#
# print(racks_used)

box_clothes = [int(num) for num in input().split()]

rack_capacity = int(input())
total_racks = 1
current_rack = []

while box_clothes:
	if sum(current_rack) + box_clothes[-1] <= rack_capacity:
		current_rack.append(box_clothes.pop())
	else:
		current_rack.clear()
		total_racks += 1

print(total_racks)

clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
new_rack_capacity = rack_capacity
racks_used = 1

for _ in range(len(clothes)):
    clothe = clothes.pop()
    if new_rack_capacity - clothe < 0:
        racks_used += 1
        new_rack_capacity = rack_capacity
    new_rack_capacity -= clothe

print(racks_used)

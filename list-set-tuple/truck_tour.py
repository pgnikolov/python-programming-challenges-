from collections import deque

pumps = int(input())

stations_values = deque([])

for _ in range(pumps):
    petrol, distance = [int(n) for n in input().split()]
    current_station_value = petrol - distance
    stations_values.append(current_station_value)

for i in range(pumps):
    all_fuel_status = [stations_values[0]]
    for j in range(1, pumps):
        all_fuel_status.append(all_fuel_status[-1] + stations_values[j])
    if all(n >= 0 for n in all_fuel_status):
        print(i)
        break
    stations_values.rotate(-1)

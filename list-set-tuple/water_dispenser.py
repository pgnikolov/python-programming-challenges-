# On the first line, you will receive the starting quantity of water (integer) in a dispenser.
# Then, on the following lines, you will be given the names of some people who want to get water
# (each on a separate line) until you receive the command "Start". Add those people to a queue.
# Finally, you will receive some commands until the command "End":
#  • "{liters}" - litters (integer) that the current person in the queue wants to get.
#     Check if there is enough water in the dispenser for that person.
#  ◦ If there is enough water, print "{person_name} got water" and remove him/her from the queue.
#  ◦ Otherwise, print "{person_name} must wait" and remove person from queue without reducing the water in dispenser.
# • "refill {liters}" - add the given litters in the dispenser.
# In the end, print how many liters of water have left in the format: "{left_liters} liters left".

from collections import deque


def water_dispenser():
    water = int(input())
    people = deque()

    # Add people to queue until "Start" command
    command = input()
    while command != "Start":
        people.append(command)
        command = input()

    # until "End"
    command = input()
    while command != "End":
        if "refill" in command:
            refill_amount = int(command.split()[1])
            water += refill_amount
        else:
            request_amount = int(command)
            if request_amount <= water:
                water -= request_amount
                print(f"{people.popleft()} got water")
            else:
                print(f"{people.popleft()} must wait")

        command = input()

    print(f"{water} liters left")


water_dispenser()

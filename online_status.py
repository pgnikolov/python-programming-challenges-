# The aim of this challenge is, given a dictionary of people's online status,
# to count the number of people who are online.
# For example, consider the following dictionary:
# statuses = {
#     "Alice": "online",
#     "Bob": "offline",
#     "Eve": "online",
# }
# In this case, the number of people online is 2.
# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings
# of names to the string "online" or "offline", as seen above.
# Your function should return the number of people who are online.

# time: 3 min 26 sec
def online_count(statuses):
    counter = 0
    for key, value in statuses.items():
        if value == "online":
            counter += 1

    return counter

# def online_count(statuses):
#     return len([stat for stat in statuses if statuses[stat] == "online"])

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    }
print(online_count(statuses))

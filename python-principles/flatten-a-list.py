# Write a function that takes a list of lists and flattens it into a one-dimensional list.
# Name your function flatten. It should take a single parameter and return a list.
# For example, calling:
# flatten([[1, 2], [3, 4]])
# Should return the list:  [1, 2, 3, 4]

# time 2 mins

def flatten(l1):
    return [char for nlist in l1 for char in nlist]


l1 = list(input())
print(flatten(l1))

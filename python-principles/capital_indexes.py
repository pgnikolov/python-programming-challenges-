# Write a function named capital_indexes. The function takes a single parameter, which is a string.
# Your function should return a list of all the indexes in the string that have capital letters.
# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

# time: 8 min 29 sec
def capital_indexes(word):
    uppercase_indices = [i for i, char in enumerate(word) if char.isupper()]
    return uppercase_indices


word = input()
print(capital_indexes(word))

# The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row.
# For example, the string "hello" has l twice in a row, while the string
# "nono" does not have two identical letters in a row.
# Define a function named double_letters that takes a single parameter. The parameter is a string.
# Your function must return True if there are two identical letters in a row in the string, and False otherwise.

# time: 22 mins
def double_letters(word):
    for i in range(len(word)):
        if word.count(word[i]) == 2:
            if word[i] == word[i - 1]:
                return True
    return False


word = str(input())
print(double_letters(word))


# def double_letters(string):
#     return any([a == b for a, b in zip(string, string[1:])])

# The goal of this challenge is to analyze a binary string consisting of only zeros and ones.
# Your code should find the biggest number of consecutive zeros in the string. For example, given the string:
# "1001101000110"
# The biggest number of consecutive zeros is 3.
# Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones.
# Your function should return the number described above.

# time 18 min
def consecutive_zeros(word):
    max_zeros = 0
    current_zeros = 0
    for n in word:
        if n == '0':
            current_zeros += 1
        else:
            max_zeros = max(max_zeros, current_zeros)
            current_zeros = 0

    max_zeros = max(max_zeros, current_zeros)

    return max_zeros


word = input()
print(consecutive_zeros(word))

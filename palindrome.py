# A string is a palindrome when it is the same when read backwards.
# For example, the string "bob" is a palindrome. So is "abba".
# But the string "abcd" is not a palindrome, because "abcd" != "dcba".
# Write a function named palindrome that takes a single string as its parameter.
# Your function should return True if the string is a palindrome, and False otherwise


# time 1 min
def palindrome(word):
    return word == word[::-1]


print(palindrome("bob"))

# Two strings are anagrams if you can make one from the other by rearranging the letters.
# Write a function named is_anagram that takes two strings as its parameters.
# Your function should return True if the strings are anagrams, and False otherwise.
# For example, the call is_anagram("typhoon", "opython") should return True
# while the call is_anagram("Alice", "Bob") should return False.

# time 19 mins

def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    return sorted(s1) == sorted(s2)


s1 = input()
s2 = input()
print(is_anagram(s1, s2))

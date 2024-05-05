# Write a function named mid that takes a string as its parameter.
# Your function should extract and return the middle letter.
# If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".

# time: 4 min 45 sec
def mid(word):
    if len(word) % 2 == 0:
        return ""
    else:
        index_mid = int((len(word) - 1) / 2)
        return word[index_mid]


word = 'abc'
print(mid(word))

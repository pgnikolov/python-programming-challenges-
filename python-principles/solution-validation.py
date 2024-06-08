# Write a function named validate that takes code represented as a string as its only parameter.
# Your function should check a few things:
# the code must contain the def keyword
# otherwise return "missing def"
# the code must contain the : symbol
# otherwise return "missing :"
# the code must contain ( and ) for the parameter list
# otherwise return "missing paren"
# the code must not contain ()
# otherwise return "missing param"
# the code must contain four spaces for indentation
# otherwise return "missing indent"
# the code must contain validate
# otherwise return "wrong name"
# the code must contain a return statement
# otherwise return "missing return"
# If all these conditions are satisfied, your code should return True.
# Here comes the twist: your solution must return True when validating itself.


# time 25 mins
def validate(word):
    if "def" not in word:
        return "missing def"
    if ":" not in word:
        return "missing :"
    if "(" not in word or ")" not in word:
        return "missing paren"
    if word.index("(") + 1 == word.index(")"):
        return "missing param"
    if "    " not in word:
        return "missing indent"
    if "validate" not in word:
        return "wrong name"
    if "return" not in word:
        return "missing return"
    else:
        return True


word = ('''def validate(word):
    if "def" not in word:
        return "missing def"
    if ":" not in word:
        return "missing :"
    if "(" not in word or ")" not in word:
        return "missing paren"
    if word.index("(") + 1 == word.index(")"):
        return "missing param"
    if "    " not in word:
        return "missing indent"
    if "validate" not in word:
        return "wrong name"
    if "return" not in word:
        return "missing return"
    else:
        return True''')

print(validate(word))

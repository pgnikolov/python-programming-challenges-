def mergeAlternately(word1: str, word2: str) -> str:
    """
    Merges two strings alternately.

    This function takes two strings, word1 and word2, and returns a new string
    where characters from word1 and word2 are interleaved. If one string is longer
    than the other, the remaining characters from the longer string are appended
    at the end.

    Parameters:
    word1 (str): The first input string.
    word2 (str): The second input string.

    Returns:
    str: The merged string.
    """

    result = []
    i = 0
    while i < len(word1) or i < len(word2):
        if i < len(word1):
            result.append(word1[i])
        if i < len(word2):
            result.append(word2[i])
        i += 1

    return ''.join(result)


class Solution:
    pass

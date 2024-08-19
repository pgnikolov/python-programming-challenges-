def reverseWords(s: str) -> str:
    trimmed_s = s.strip()
    words = trimmed_s.split()
    reversed_words = words[::-1]
    result = ' '.join(reversed_words)

    return result


# Example usage
print(reverseWords("the sky is blue"))  # Output: "blue is sky the"
print(reverseWords("  hello world  "))  # Output: "world hello"
print(reverseWords("a good   example"))  # Output: "example good a"

def isValid(s):
    """
    Check if the input string is a valid parentheses, brackets, or curly braces sequence.

    Parameters:
    s (str): The input string to be checked.

    Returns:
    bool: True if the input string is valid, False otherwise.
    """
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack

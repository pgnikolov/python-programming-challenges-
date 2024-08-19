def romanToInt(s: str) -> int:
    # Dictionary mapping Roman numerals to their integer values
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    # Traverse the string from left to right
    for char in s:
        # Get the integer value for the current Roman numeral
        current_value = roman_to_int[char]

        # If the previous value is less than the current value, subtract the previous value twice
        if prev_value < current_value:
            total += current_value - 2 * prev_value
        else:
            total += current_value

        # Update the previous value to the current value
        prev_value = current_value

    return total

# Example usage:
print(romanToInt("III"))       # Output: 3
print(romanToInt("LVIII"))     # Output: 58
print(romanToInt("MCMXCIV"))   # Output: 1994

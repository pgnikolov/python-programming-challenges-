def print_rangoli(n):
    import string
    alphabet = string.ascii_lowercase

    # Calculate the width of the rangoli
    max_width = 4 * n - 3

    # Create the list to hold all the rows
    rangoli_lines = []

    for i in range(n):
        s = '-'.join(alphabet[n - 1:i:-1] + alphabet[i:n])
        rangoli_lines.append(s.center(max_width, '-'))

    # Combine top and bottom parts
    full_rangoli = rangoli_lines[::-1] + rangoli_lines[1:]

    # Join all rows into a single string with newlines and print it
    print('\n'.join(full_rangoli))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
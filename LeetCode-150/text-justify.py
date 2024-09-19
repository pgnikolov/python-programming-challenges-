def fullJustify(words, maxWidth):
    def justify_line(line, maxWidth, is_last_line):
        if len(line) == 1 or is_last_line:
            return ' '.join(line).ljust(maxWidth)

        total_chars = sum(len(word) for word in line)
        total_spaces = maxWidth - total_chars
        num_gaps = len(line) - 1

        even_space = total_spaces // num_gaps
        extra_space = total_spaces % num_gaps

        justified_line = ''
        for i in range(num_gaps):
            justified_line += line[i]
            justified_line += ' ' * (even_space + (1 if i < extra_space else 0))
        justified_line += line[-1]  # Append the last word

        return justified_line

    result = []
    current_line = []
    current_length = 0

    for word in words:
        word_length = len(word)

        if current_length + len(current_line) + word_length <= maxWidth:
            current_line.append(word)
            current_length += word_length
        else:
            result.append(justify_line(current_line, maxWidth, False))
            current_line = [word]
            current_length = word_length

    if current_line:
        result.append(justify_line(current_line, maxWidth, True))

    return result


# Example usage:
print(fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16))
print(fullJustify(
    ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art",
     "is", "everything", "else", "we", "do"], 20))

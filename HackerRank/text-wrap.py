import textwrap


def wrap(string, max_width):
    wrapped_lines = textwrap.wrap(string, width=max_width)
    return '\n'.join(wrapped_lines)

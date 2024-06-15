# Complete the solve function below.
def solve(s):
    words = s.split()
    capitalized_words = [word.capitalize() if word[0].isalpha() else word for word in words]
    return ' '.join(capitalized_words)


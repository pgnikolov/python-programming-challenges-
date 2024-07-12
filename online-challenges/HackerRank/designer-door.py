# Enter your code here. Read input from STDIN. Print output to STDOUT
def create_mat(n, m):
    # Top half
    for i in range(1, n, 2):
        pattern = ".|." * i
        print(pattern.center(m, '-'))

    # Center
    print("WELCOME".center(m, '-'))

    # Bottom half
    for i in range(n - 2, -1, -2):
        pattern = ".|." * i
        print(pattern.center(m, '-'))


# Example usage:
n, m = map(int, input().split())
create_mat(n, m)

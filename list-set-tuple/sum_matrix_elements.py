# rite a program that reads a matrix from the console and prints:
#     • The sum of all numbers in the matrix
#     • The matrix itself
# On the first line, you will receive the matrix sizes in the format "{rows}, {columns}".
# On the next rows, you will get elements for each column separated by a comma and a space ", ".

rows, cols = map(int, input().split(', '))

matrix = []
for i in range(rows):
    matrix.append([int(num) for num in input().split(", ")])

total_sum = 0
for i in range(rows):
    for j in range(cols):
        total_sum += matrix[i][j]

print(total_sum)
print(matrix)

n = int(input())

matrix = []

for _ in range(n):
    matrix.append(input())

symbol = input()

for row in range(n):
    for column in range(n):
        if symbol in matrix[row][column]:
            print(f"({row}, {column})")
            exit()

print(f"{symbol} does not occur in the matrix")
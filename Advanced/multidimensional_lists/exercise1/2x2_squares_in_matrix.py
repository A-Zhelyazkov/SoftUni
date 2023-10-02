rows, columns = [int(i) for i in input().split()]

matrix = [input().split() for _ in range(rows)]

occurences = 0

for r in range(rows-1):
    for c in range(columns-1):
        letter = matrix[r][c]
        next_to = matrix[r][c+1]
        below = matrix[r+1][c]
        diagonal = matrix[r+1][c+1]

        if letter == next_to == below == diagonal:
            occurences += 1

print(occurences)
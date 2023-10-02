rows, columns = [int(i) for i in input().split(", ")]

matrix = []
sum_nums = 0
highest_sum = float('-inf')
for _ in range(rows):
    matrix.append([int(i) for i in input().split(", ")])

for row in range(rows-1):
    for column in range(columns-1):
        current_symb = matrix[row][column]
        next_to = matrix[row][column + 1]
        below = matrix[row+1][column]
        diag = matrix[row + 1][column + 1]
        current_sum = current_symb + next_to + below + diag

        if current_sum > highest_sum:
            highest_sum = current_sum
            sub_mat = [[current_symb, next_to], [below, diag]]

for i in sub_mat:
    print(*i)
print(highest_sum)

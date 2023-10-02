rows, columns = [int(i) for i in input().split()]

matrix = [[int(i) for i in input().split()] for _ in range(rows)]
max_sum = float("-inf")
for r in range(rows-2):
    current_sum = 0
    for c in range(columns-2):
        num = matrix[r][c]
        next_to_1 = matrix[r][c+1]
        next_to_2 = matrix[r][c+2]
        below_1 = matrix[r+1][c]
        below_2 = matrix[r+2][c]
        diag_1 = matrix[r+1][c+1]
        diag_2 = matrix[r+2][c+2]
        random_1 = matrix[r+1][c+2]
        random_2 = matrix[r+2][c+1]

        current_sum = num + next_to_1 + next_to_2 + diag_1 + diag_2 + random_1 + random_2 + below_1 + below_2

        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [[num, next_to_1, next_to_2], [below_1, diag_1, random_1], [below_2, random_2, diag_2]]


print(f"Sum = {max_sum}")
for i in sub_matrix:
    print(*i)


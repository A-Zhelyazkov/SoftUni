rows, columns = [int(i) for i in input().split(", ")]

matrix = []
sum_nums = 0
for _ in range(rows):
    matrix.append([int(i) for i in input().split(" ")])

for column in range(columns):
    current_sum = 0
    for row in range(rows):
        current_sum += matrix[row][column]

    print(current_sum)
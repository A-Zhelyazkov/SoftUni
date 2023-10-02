rows = int(input())

matrix = []
sum_nums = 0
for _ in range(rows):
    matrix.extend([int(i) for i in input().split(", ")])

print(matrix)
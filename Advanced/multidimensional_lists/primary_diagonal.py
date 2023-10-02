rows = int(input())

matrix = []
final_sum = 0
for _ in range(rows):
    matrix.append([int(i) for i in input().split()])

for i in range(rows):
    final_sum += matrix[i][i]

print(final_sum)
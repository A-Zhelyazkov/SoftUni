rows, columns = [int(i) for i in input().split(", ")]

matrix = []
sum_nums = 0
for _ in range(rows):
    line = [int(i) for i in input().split(", ")]
    sum_nums += sum(line)
    matrix.append(line)

print(sum_nums)
print(matrix)
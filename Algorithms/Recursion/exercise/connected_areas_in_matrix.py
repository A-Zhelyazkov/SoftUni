def extract_size(area_string):
    return int(area_string.split("size:")[1].strip())


def is_valid_row_col(r, c, map):
    if r < 0 or c < 0 or r >= len(map) or c >= len(map[0]):
        return False
    return True

def find_area(row, col, matrix):
    if not is_valid_row_col(row, col, matrix):
        return 0

    if matrix[row][col] != '-':
        return 0

    matrix[row][col] = 'o'

    size = 1
    size += find_area(row + 1, col, matrix)
    size += find_area(row - 1, col, matrix)
    size += find_area(row , col + 1, matrix)
    size += find_area(row , col - 1, matrix)

    return size

rows = int(input())
cols = int(input())
matrix = []
for _ in range(rows):
    matrix.append(list(input()))

answers = []

for r in range(rows):
    for c in range(cols):
        field = find_area(r, c, matrix)
        if field > 0:
            answers.append([r, c, field])

answers = sorted(answers, key=lambda s: -s[2])

current_area = 0
print(f"Total areas found: {len(answers)}")
for area in answers:
    current_area += 1
    print(f"Area #{current_area} at ({area[0]}, {area[1]}), size: {area[2]}")

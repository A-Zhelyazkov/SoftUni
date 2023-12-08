def is_valid_location(row, col, field):
    if row>= len(field) or col>= len(field[0]) or field[row][col] == 'v':
        return False
    return True

def find_all_paths(row, col, field):
    global total_ways
    if not is_valid_location(row, col, field):
        return

    if field[row][col] == 'f':
        total_ways += 1

    else:
        field[row][col] = 'v'
        find_all_paths(row+1, col, field)
        find_all_paths(row, col+1, field)
        field[row][col] = None
rows = int(input())
cols = int(input())
field = []
total_ways = 0

for c in range(rows):
    field.append([None] * cols)

    if c+1 == rows:
        field[c][cols-1] = 'f'


find_all_paths(0, 0, field)
print(total_ways)
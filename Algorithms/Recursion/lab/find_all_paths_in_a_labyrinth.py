def is_valid_location(row, col, lab):
    if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]) or lab[row][col] == "*" or lab[row][col] == 'v':
        return False
    return True

def find_all_paths(rows, cols, lab, direction, path):
    if not is_valid_location(rows, cols, lab):
        return


    path.append(direction)

    if lab[rows][cols] == 'e':
        print(''.join(path))
    else:
        lab[rows][cols] = 'v'
        find_all_paths(rows + 1, cols, lab, 'D', path)
        find_all_paths(rows - 1, cols, lab, 'U', path)
        find_all_paths(rows, cols + 1, lab, 'R', path)
        find_all_paths(rows, cols - 1, lab, 'L', path)
        lab[rows][cols] = '-'

    path.pop()


rows = int(input())
cols = int(input())

lab = []

for row in range(rows):
    lab.append(list(input()))


find_all_paths(0, 0, lab, '', [])
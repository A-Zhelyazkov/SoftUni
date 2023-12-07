def gen_01_vect(map, idx):
    if idx == len(map):
        print(*map, sep='')
        return

    for i in range(2):
        map[idx] = i
        gen_01_vect(map, idx + 1)


num = int(input())

map = [0] * num

gen_01_vect(map, 0)
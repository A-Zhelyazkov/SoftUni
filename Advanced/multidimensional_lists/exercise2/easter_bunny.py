n = int(input())

field = []
bunny_pos = []

for row in range(n):
    field.append(input().split())

    if 'B' in field[row]:
        bunny_pos = [row, field[row].index('B')]

print(field)
print(bunny_pos)




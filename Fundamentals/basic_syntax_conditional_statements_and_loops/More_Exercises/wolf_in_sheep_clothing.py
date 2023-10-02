animals = input()

list_animals = [animals]
reversed_list = list_animals[-1:]

print(reversed_list)

while len(list_animals) > 0:
    list.pop(list_animals)
nums = input()
list_of_strings = nums.split(' ')
list_of_integers = list(map(int, list_of_strings))
opposite = []
for i in list_of_integers:
    opposite.append(-i)

print(opposite)
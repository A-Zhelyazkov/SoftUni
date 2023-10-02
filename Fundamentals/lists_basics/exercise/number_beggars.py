values_string = input().split(', ')
beggars = int(input())
values_ints = [int(i) for i in values_string]
final_list = []
current_beggar = 0

while current_beggar < beggars:
    sum_for_current_beggar = 0
    for index in range(current_beggar, len(values_ints), beggars):
        sum_for_current_beggar += values_ints[index]
    current_beggar += 1
    final_list.append(sum_for_current_beggar)

print(final_list)
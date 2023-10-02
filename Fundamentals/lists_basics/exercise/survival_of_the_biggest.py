list_input = input().split()
count = int(input())
list_input_ints = [int(i) for i in list_input]

for i in range(count):
    min_num = min(list_input_ints)
    list_input_ints.remove(min_num)

list_input_string = [str(i) for i in list_input_ints]
print(', '.join(list_input_string))
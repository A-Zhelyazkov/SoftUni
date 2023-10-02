n = int(input())
special_word = input()
list_strings = []
special_list = []
for i in range(n):
    examples = input()
    list_strings.append(examples)
    if special_word in examples:
        special_list.append(examples)

print(list_strings)
print(special_list)

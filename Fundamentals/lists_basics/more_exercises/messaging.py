numbers = input().split()
message = input()
outputs = []
for i in numbers:
    sum_of_chars = 0
    for ch in i:
        sum_of_chars += int(ch)
    needed_index = sum_of_chars % (len(message))
    needed_char = message[needed_index]
    message = message.replace(needed_char, '', 1)
    outputs.append(needed_char)

print(''.join(outputs))



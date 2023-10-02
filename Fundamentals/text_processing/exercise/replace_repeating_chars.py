text = input()
final_str = ''
last_letter = ''

for current in text:
    if current != last_letter:
        final_str += current
        last_letter = current

print(final_str)
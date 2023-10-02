text_input = input()

occurences_text = {}

for i in text_input:
    if i not in occurences_text:
        occurences_text[i] = 0

    occurences_text[i] += 1

sorted_dict = sorted(occurences_text.items())

for i in sorted_dict:
    print(f"{i[0]}: {i[1]} time/s")
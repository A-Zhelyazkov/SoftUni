message = input().split()
final_word = []

for i in message:
    num = ''
    for ch in i:
        if ch.isdigit():
            num += ch

        else:
            break

    first_letter = chr(int(num))
    current_word = first_letter + ''.join([k for k in i if not k.isdigit()])
    current_word_list = [i for i in current_word]
    current_word_list[1], current_word_list[-1] = current_word_list[-1], current_word_list[1]
    final_word.append(''.join(current_word_list))

print(' '.join(final_word))



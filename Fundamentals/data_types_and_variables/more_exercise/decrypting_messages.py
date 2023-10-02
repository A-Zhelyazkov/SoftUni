key = int(input())
lines = int(input())
final_word = []
for i in range(lines):
    letters = input()
    ascii_letter = ord(letters) + key
    list.append(final_word, chr(ascii_letter))

print("".join(final_word))
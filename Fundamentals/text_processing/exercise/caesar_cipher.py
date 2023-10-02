text = input()
encrypted_text = ''

for i in text:
    encrypted_word = ord(i) + 3
    encrypted_text += chr(encrypted_word)

print(encrypted_text)
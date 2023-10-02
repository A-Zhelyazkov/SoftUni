deleted_string = input()
word = input()

while deleted_string in word:
    word = word.replace(deleted_string, '')

print(word)
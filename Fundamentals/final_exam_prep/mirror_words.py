import re

text = input()

pattern = r'([@#])([a-zA-Z]{3,})\1{2,}([a-zA-Z]{3,})\1'

matches = re.findall(pattern, text)
match_words = []
for i in matches:
    word1 = i[1]
    word2 = i[2]

    word2_backward = word2[::-1]

    if word1 == word2_backward:
        match_words.append(f"{word1} <=> {word2}")

if not matches:
    print(f"No word pairs founds!")
else:
    print(f"{len(matches)} word pairs found!")

if not match_words:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(', '.join(match_words))


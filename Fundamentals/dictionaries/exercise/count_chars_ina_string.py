word = input().replace(" ", "")
text = {i: 0 for i in word}

for i in word:
    text[i] += 1

for key, value in text.items():
    print(f"{key} -> {value}")
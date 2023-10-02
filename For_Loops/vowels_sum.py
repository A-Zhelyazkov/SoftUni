word = input()
total = 0

for vowel in word:
    if vowel == "a":
        total += 1
    elif vowel == "e":
        total += 2
    elif vowel == "i":
        total += 3
    elif vowel == "o":
        total += 4
    elif vowel == "u":
        total += 5

print(total)

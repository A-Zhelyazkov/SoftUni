from collections import deque

vowels = deque([i for i in input().split()])
consonants = deque([i for i in input().split()])

words = {
    "rose": "rose",
    "tulip": "tulip",
    "lotus": "lotus",
    "daffodil": "daffodil",
}

words_copy = words.copy()

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for word in words:
        words[word] = words[word].replace(vowel, '')
        words[word] = words[word].replace(consonant, '')
        if words[word] == '':
            print(f"Word found: {words_copy[word]}")
            if vowels:
                print(f"Vowels left: {' '.join(vowels)}")
            if consonants:
                print(f"Consonants left: {' '.join(consonants)}")
            raise SystemExit


print(f"Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
def smaller_num(a, b):
    if len(a) > len(b):
        return b
    elif len(b) > len(a):
        return a
    else:
        return a


word1, word2 = input().split()
result = 0

for i in range(len(smaller_num(word1, word2))):
    result += ord(word1[i]) * ord(word2[i])

if len(word1) > len(word2):
    for i in range(len(word2), len(word1)):
        result += ord(word1[i])

elif len(word1) < len(word2):
    for i in range(len(word1), len(word2)):
        result += ord(word2[i])
print(result)


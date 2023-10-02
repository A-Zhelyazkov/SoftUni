sequence = input().split()
result = []

for word in sequence:
    result.append(word * len(word))

print(''.join(result))
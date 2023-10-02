sequence = input().split(", ")
sorted_sequence = sorted(sequence, key=lambda x: (-len(x), x))
print(sorted_sequence)

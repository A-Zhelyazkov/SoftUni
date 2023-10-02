sequence = [int(i) for i in input().split(', ')]
even_indexes = [i for i in range(len(sequence)) if sequence[i] % 2 == 0]
print(even_indexes)
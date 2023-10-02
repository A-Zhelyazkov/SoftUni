rows, columns = [int(i) for i in input().split()]

matrix = [['' for _ in range(columns)] for _ in range(rows)]

for row in range(rows):
    first_letter = chr(ord('a') + row)
    for col in range(columns):
        middle_letter = chr(ord(first_letter) + col)
        palindrome = first_letter + middle_letter + first_letter
        matrix[row][col] = palindrome

for i in matrix:
    print(*i)


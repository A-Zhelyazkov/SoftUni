first_char = ord(input())
second_char = ord(input())
sequence = input()
result = 0
lower_boundary = min(first_char, second_char)
upper_boundary = max(first_char, second_char)

for i in sequence:
    if lower_boundary < ord(i) < upper_boundary:
        result += ord(i)

print(result)
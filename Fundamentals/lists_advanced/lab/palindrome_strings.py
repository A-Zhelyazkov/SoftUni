sequence = input().split()
palindrome = input()
final_list = []
counter = 0
for el in sequence:
    if el == ''.join(reversed(el)):
        final_list.append(el)
    if el == palindrome:
        counter += 1

print(final_list)
print(f"Found palindrome {counter} times")


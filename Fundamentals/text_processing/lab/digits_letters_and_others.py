text = input()

nums, letters, other = [], [], []

for i in text:
    if i.isdigit():
        nums.append(i)
    elif i.isalpha():
        letters.append(i)
    else:
        other.append(i)

print(''.join(nums))
print(''.join(letters))
print(''.join(other))

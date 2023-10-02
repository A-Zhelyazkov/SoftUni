import re
n = int(input())
pattern_digits = r'\d'
for _ in range(n):
    text = input()

    pattern = r'@[#]{1,}([A-Z][a-zA-Z0-9]{4,}[A-Z])@[#]{1,}'

    matches = re.findall(pattern, text)
    if not matches:
        print(f"Invalid barcode")
        continue

    digits = ''

    for word in matches:
        for char in word:
            if char.isdigit():
                digits += char
            else:
                continue

    if digits:
        print(f"Product group: {digits}")
    else:
        print(f"Product group: 00")
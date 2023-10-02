import re

n = int(input())
pattern = r'!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})]'

for _ in range(n):
    text = input()

    matches = re.findall(pattern, text)
    final_message = []

    if matches:
        data = matches[0]
        message = data[1]
        for i in message:
            final_message.append(str(ord(i)))

        print(f"{data[0]}: {' '.join(final_message)}")

    else:
        print("The message is invalid")



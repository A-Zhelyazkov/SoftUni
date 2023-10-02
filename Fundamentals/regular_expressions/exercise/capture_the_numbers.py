import re


while True:
    text = input()

    if not text:
        break

    pattern = r"\d+"

    result = re.findall(pattern, text)

    for i in result:
        print(i, end=" ")
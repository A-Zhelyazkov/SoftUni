import re
pattern = r"(www\.[a-zA-Z0-9\-]+(\.[a-z]+)+)"
while True:
    command = input()

    if not command:
        break

    result = re.findall(pattern, command)

    if result:
        for i in result:
            print(i[0])
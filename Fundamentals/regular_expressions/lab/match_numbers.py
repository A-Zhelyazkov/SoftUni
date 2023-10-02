import re

numbers = input()

pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'

results = re.finditer(pattern, numbers)

for i in results:
    print(i.group(), end=' ')

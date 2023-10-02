import re

names = input()
pattern = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b"
result = re.findall(pattern, names)

print(' '.join(result))

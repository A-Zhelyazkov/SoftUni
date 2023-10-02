import re

dates = input()

pattern = r'\b([\d]{2})([/.-])([A-Z][a-z]{2})\2([\d]{4})\b'

result = re.findall(pattern, dates)

for i in result:
    print(f"Day: {i[0]}, Month: {i[2]}, Year: {i[3]}")